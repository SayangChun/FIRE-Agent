"""Tests for compound_calculator.py."""

import pytest

from tools.compound_calculator import (
    future_value,
    future_value_real,
    compound_growth_series,
)


class TestFutureValue:
    """Tests for future_value."""

    def test_future_value_no_contributions(self):
        """100000 at 7% for 10 years (no contributions)."""
        result = future_value(100_000, 0, 0.07, 10)
        # 100000 * (1.07)^10 ≈ 196715
        expected = 100_000 * (1.07 ** 10)
        assert result["nominal_value"] == pytest.approx(expected, rel=1e-3)
        assert result["total_contributed"] == 100_000
        assert result["fv_contributions"] == 0

    def test_future_value_with_contributions(self):
        """Monthly additions should increase final value."""
        result = future_value(100_000, 1_000, 0.07, 10)
        assert result["nominal_value"] > 100_000
        assert result["total_contributed"] == 100_000 + 1_000 * 120
        assert result["total_growth"] > 0

    def test_future_value_zero_return(self):
        """0% return -> total = contributions only."""
        result = future_value(100_000, 1_000, 0.0, 10)
        expected = 100_000 + 1_000 * 120
        assert result["nominal_value"] == pytest.approx(expected, rel=1e-6)
        assert result["total_growth"] == pytest.approx(0, abs=1)

    def test_future_value_negative_return(self):
        """Negative return should decrease value."""
        result = future_value(100_000, 0, -0.03, 10)
        assert result["nominal_value"] < 100_000

    def test_future_value_invalid_return(self):
        """Return < -1 should raise ValueError."""
        with pytest.raises(ValueError):
            future_value(100_000, 0, -1.5, 10)

    def test_future_value_invalid_years(self):
        """Negative years should raise ValueError."""
        with pytest.raises(ValueError):
            future_value(100_000, 0, 0.07, -1)

    def test_future_value_growth_multiple(self):
        """Growth multiple = nominal / contributed."""
        result = future_value(100_000, 0, 0.07, 10)
        expected = result["nominal_value"] / 100_000
        # growth_multiple is rounded to 2 decimal places in the source
        assert result["growth_multiple"] == round(expected, 2)


class TestFutureValueReal:
    """Tests for future_value_real."""

    def test_future_value_real_inflation_adjustment(self):
        """Real value should be less than nominal (inflation eats value)."""
        result = future_value_real(100_000, 1_000, 0.07, 0.025, 10)
        assert result["real_value"] < result["nominal_value"]
        assert result["inflation_factor"] == pytest.approx(1.025 ** 10, rel=1e-4)

    def test_future_value_real_zero_inflation(self):
        """Zero inflation -> real == nominal."""
        result = future_value_real(100_000, 0, 0.07, 0.0, 10)
        assert result["real_value"] == pytest.approx(result["nominal_value"], rel=1e-6)

    def test_future_value_real_keys(self):
        """Result should contain expected keys."""
        result = future_value_real(100_000, 1_000, 0.07, 0.025, 10)
        assert "nominal_value" in result
        assert "real_value" in result
        assert "inflation_factor" in result
        assert "real_growth" in result


class TestCompoundGrowthSeries:
    """Tests for compound_growth_series."""

    def test_compound_growth_series_length(self):
        """Series length should be years + 1 (includes year 0)."""
        result = compound_growth_series(100_000, 0, 0.07, 30)
        assert len(result) == 31

    def test_compound_growth_series_first_year(self):
        """Year 0 should equal starting assets."""
        result = compound_growth_series(100_000, 0, 0.07, 10)
        assert result[0]["year"] == 0
        assert result[0]["assets"] == 100_000

    def test_compound_growth_series_monotonic(self):
        """Assets should increase over time with positive return."""
        result = compound_growth_series(100_000, 1_000, 0.07, 10)
        for i in range(1, len(result)):
            assert result[i]["assets"] >= result[i - 1]["assets"]

    def test_compound_growth_series_contributed(self):
        """Contributed field should equal initial + monthly * 12 * year."""
        result = compound_growth_series(100_000, 1_000, 0.07, 5)
        for entry in result:
            expected = 100_000 + 1_000 * 12 * entry["year"]
            assert entry["contributed"] == pytest.approx(expected, rel=1e-6)

    def test_compound_growth_series_keys(self):
        """Each entry should have year, assets, contributed."""
        result = compound_growth_series(50_000, 500, 0.07, 5)
        for entry in result:
            assert "year" in entry
            assert "assets" in entry
            assert "contributed" in entry
