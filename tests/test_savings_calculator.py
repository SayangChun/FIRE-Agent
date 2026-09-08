"""Tests for savings_calculator.py."""

import pytest

from tools.savings_calculator import (
    annual_savings,
    calculate_savings_rate,
    savings_rate_sensitivity,
)


class TestAnnualSavings:
    """Tests for annual_savings."""

    def test_savings_basic(self):
        """100000 - 60000 = 40000."""
        assert annual_savings(100_000, 60_000) == 40_000

    def test_savings_equal(self):
        """Income equals expenses -> 0 savings."""
        assert annual_savings(60_000, 60_000) == 0

    def test_savings_negative(self):
        """Expenses exceed income -> negative savings."""
        assert annual_savings(50_000, 60_000) == -10_000


class TestCalculateSavingsRate:
    """Tests for calculate_savings_rate."""

    def test_savings_rate_basic(self):
        """100000 income, 60000 expenses = 40%."""
        result = calculate_savings_rate(100_000, 60_000)
        assert result["savings_rate"] == pytest.approx(0.4, abs=1e-6)
        assert result["annual_savings"] == 40_000
        assert result["monthly_savings"] == pytest.approx(40_000 / 12, abs=0.01)

    def test_savings_rate_zero_income(self):
        """Zero income should handle gracefully (rate = 0)."""
        result = calculate_savings_rate(0, 30_000)
        assert result["savings_rate"] == 0
        assert result["annual_savings"] == -30_000

    def test_savings_rate_negative(self):
        """Expenses > income -> negative savings rate."""
        result = calculate_savings_rate(50_000, 60_000)
        assert result["savings_rate"] == pytest.approx(-0.2, abs=1e-6)
        assert result["annual_savings"] == -10_000

    def test_savings_rate_50pct(self):
        """Exact 50% savings rate."""
        result = calculate_savings_rate(100_000, 50_000)
        assert result["savings_rate"] == pytest.approx(0.5, abs=1e-6)

    def test_savings_rate_negative_income(self):
        """Negative income should raise ValueError."""
        with pytest.raises(ValueError):
            calculate_savings_rate(-10_000, 30_000)

    def test_savings_rate_diagnostic_negative(self):
        """Negative savings should produce warning diagnostic."""
        result = calculate_savings_rate(50_000, 60_000)
        assert any("negative" in d.lower() for d in result["diagnostics"])

    def test_savings_rate_diagnostic_low(self):
        """Low savings rate should produce suggestion diagnostic."""
        result = calculate_savings_rate(100_000, 85_000)
        assert any("20%" in d for d in result["diagnostics"])

    def test_savings_rate_diagnostic_excellent(self):
        """High savings rate should produce excellent diagnostic."""
        result = calculate_savings_rate(100_000, 30_000)
        assert any("excellent" in d.lower() for d in result["diagnostics"])

    def test_savings_rate_returns_keys(self):
        """Result should contain expected keys."""
        result = calculate_savings_rate(100_000, 60_000)
        assert "savings_rate" in result
        assert "savings_rate_pct" in result
        assert "annual_savings" in result
        assert "monthly_savings" in result
        assert "diagnostics" in result


class TestSavingsRateSensitivity:
    """Tests for savings_rate_sensitivity."""

    def test_sensitivity_default_rates(self):
        """Default target rates should produce 6 results."""
        results = savings_rate_sensitivity(100_000, 60_000)
        assert len(results) == 6
        rates = [r["target_rate"] for r in results]
        assert rates == [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    def test_sensitivity_custom_rates(self):
        """Custom target rates."""
        results = savings_rate_sensitivity(100_000, 60_000, target_rates=[0.5, 0.7])
        assert len(results) == 2

    def test_sensitivity_expense_reduction(self):
        """Higher target rate requires lower expenses -> expense reduction."""
        results = savings_rate_sensitivity(100_000, 60_000)
        for i in range(1, len(results)):
            assert results[i]["required_annual_expenses"] <= results[i - 1]["required_annual_expenses"]
