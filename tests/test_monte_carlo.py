"""Tests for monte_carlo.py."""

import pytest

from tools.monte_carlo import run_monte_carlo, MonteCarloResult


class TestMonteCarloReproducibility:
    """Tests for seed-based reproducibility."""

    def test_monte_carlo_reproducible(self):
        """Same seed should produce identical results."""
        r1 = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=100)
        r2 = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=100)
        assert r1.success_probability == r2.success_probability
        assert r1.median_final_assets == r2.median_final_assets
        assert r1.percentiles == r2.percentiles

    def test_monte_carlo_different_seeds(self):
        """Different seeds should produce different results."""
        r1 = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=1000)
        r2 = run_monte_carlo(1_000_000, 40_000, seed=99, simulations=1000)
        # Not guaranteed to differ, but very likely with different seeds
        assert r1.success_probability != r2.success_probability


class TestMonteCarloProperties:
    """Tests for mathematical properties of Monte Carlo results."""

    def test_monte_carlo_success_range(self):
        """Success probability must be between 0 and 1."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=500)
        assert 0 <= result.success_probability <= 1

    def test_monte_carlo_success_failure_sum(self):
        """Success + failure probabilities must sum to 1."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=500)
        assert result.success_probability + result.failure_probability == pytest.approx(1.0)

    def test_monte_carlo_high_assets(self):
        """High assets should produce high success probability."""
        result = run_monte_carlo(
            10_000_000, 40_000, seed=42, simulations=100, years=30
        )
        assert result.success_probability >= 0.95

    def test_monte_carlo_low_assets(self):
        """Low assets should produce low success probability."""
        result = run_monte_carlo(
            100_000, 40_000, seed=42, simulations=100, years=30
        )
        assert result.success_probability <= 0.1


class TestMonteCarloPercentiles:
    """Tests for percentile ordering."""

    def test_monte_carlo_percentiles_ordering(self):
        """p10 <= p25 <= p50 <= p75 <= p90."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=1000)
        p = result.percentiles
        assert p["p10"] <= p["p25"]
        assert p["p25"] <= p["p50"]
        assert p["p50"] <= p["p75"]
        assert p["p75"] <= p["p90"]

    def test_monte_carlo_percentiles_non_negative(self):
        """Percentiles should be non-negative (assets)."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=100)
        for key in ["p10", "p25", "p50", "p75", "p90"]:
            assert result.percentiles[key] >= 0


class TestMonteCarloResult:
    """Tests for MonteCarloResult class."""

    def test_to_dict_keys(self):
        """to_dict should return expected keys."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=100)
        d = result.to_dict()
        assert "success_probability" in d
        assert "failure_probability" in d
        assert "median_final_assets" in d
        assert "percentiles" in d
        assert "simulations" in d
        assert "years" in d

    def test_to_dict_probability_pct_format(self):
        """to_dict should include formatted percentage strings."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=100)
        d = result.to_dict()
        assert "%" in d["success_probability_pct"]
        assert "%" in d["failure_probability_pct"]

    def test_simulations_count(self):
        """Simulations count should match input."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, simulations=200)
        assert result.simulations == 200

    def test_years_count(self):
        """Years should match input."""
        result = run_monte_carlo(1_000_000, 40_000, seed=42, years=20)
        assert result.years == 20
