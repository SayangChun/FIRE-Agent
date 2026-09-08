"""Tests for fire_calculator.py."""

import pytest

from tools.fire_calculator import (
    calculate_fire_number,
    fire_number_sensitivity,
    calculate_fire_progress,
    estimate_fire_age,
    reverse_fire_plan,
)


class TestCalculateFireNumber:
    """Tests for calculate_fire_number."""

    def test_fire_number_basic(self):
        """60000 / 0.04 = 1500000."""
        result = calculate_fire_number(60000, 0.04)
        assert result["fire_number"] == 1_500_000

    def test_fire_number_3pct(self):
        """60000 / 0.03 = 2000000."""
        result = calculate_fire_number(60000, 0.03)
        assert result["fire_number"] == 2_000_000

    def test_fire_number_zero_expenses(self):
        """0 / 0.04 = 0."""
        result = calculate_fire_number(0, 0.04)
        assert result["fire_number"] == 0

    def test_fire_number_invalid_rate(self):
        """Withdrawal rate <= 0 should raise ValueError."""
        with pytest.raises(ValueError):
            calculate_fire_number(60000, 0)
        with pytest.raises(ValueError):
            calculate_fire_number(60000, -0.04)

    def test_fire_number_negative_expenses(self):
        """Negative expenses should raise ValueError."""
        with pytest.raises(ValueError):
            calculate_fire_number(-10000, 0.04)

    def test_fire_number_returns_correct_keys(self):
        """Result should contain expected keys."""
        result = calculate_fire_number(60000, 0.04)
        assert "fire_number" in result
        assert "withdrawal_rate" in result
        assert "annual_retirement_expenses" in result

    def test_fire_number_sensitivity(self):
        """Test default sensitivity rates."""
        results = fire_number_sensitivity(60000)
        assert len(results) == 6
        rates = [r["withdrawal_rate"] for r in results]
        assert rates == [0.025, 0.03, 0.035, 0.04, 0.045, 0.05]
        for r in results:
            assert r["fire_number"] == round(60000 / r["withdrawal_rate"], 2)

    def test_fire_number_sensitivity_custom_rates(self):
        """Test sensitivity with custom rates."""
        results = fire_number_sensitivity(60000, rates=[0.03, 0.05])
        assert len(results) == 2


class TestCalculateFireProgress:
    """Tests for calculate_fire_progress."""

    def test_fire_progress_50pct(self):
        """750000 / 1500000 = 0.5."""
        result = calculate_fire_progress(750_000, 1_500_000)
        assert result["progress"] == pytest.approx(0.5, abs=1e-6)

    def test_fire_progress_100pct(self):
        """1500000 / 1500000 = 1.0."""
        result = calculate_fire_progress(1_500_000, 1_500_000)
        assert result["progress"] == pytest.approx(1.0, abs=1e-6)
        assert result["remaining"] == 0

    def test_fire_progress_overfunded(self):
        """2000000 / 1500000 = 1.333."""
        result = calculate_fire_progress(2_000_000, 1_500_000)
        assert result["progress"] == pytest.approx(2_000_000 / 1_500_000, abs=1e-6)
        assert result["remaining"] == 0

    def test_fire_progress_zero_assets(self):
        """0 assets -> 0% progress."""
        result = calculate_fire_progress(0, 1_500_000)
        assert result["progress"] == 0
        assert result["remaining"] == 1_500_000

    def test_fire_progress_invalid_fire_number(self):
        """fire_number <= 0 should raise ValueError."""
        with pytest.raises(ValueError):
            calculate_fire_progress(100_000, 0)


class TestEstimateFireAge:
    """Tests for estimate_fire_age."""

    def test_estimate_fire_age_basic(self):
        """Test with known inputs."""
        result = estimate_fire_age(
            current_age=30,
            current_assets=100_000,
            monthly_contribution=2_000,
            annual_return=0.07,
            fire_number=1_500_000,
        )
        assert result["reached"] is True
        assert result["estimated_fire_age"] is not None
        assert result["years_remaining"] is not None
        assert result["years_remaining"] > 0

    def test_estimate_fire_age_already_funded(self):
        """Current assets already exceed fire_number."""
        result = estimate_fire_age(
            current_age=30,
            current_assets=2_000_000,
            monthly_contribution=0,
            annual_return=0.07,
            fire_number=1_500_000,
        )
        assert result["reached"] is True
        assert result["years_remaining"] == 0
        assert result["estimated_fire_age"] == 30

    def test_estimate_fire_age_invalid_fire_number(self):
        """fire_number <= 0 should raise ValueError."""
        with pytest.raises(ValueError):
            estimate_fire_age(30, 100_000, 2000, 0.07, 0)


class TestReverseFirePlan:
    """Tests for reverse_fire_plan."""

    def test_reverse_fire_plan_basic(self):
        """Test required monthly contribution with known inputs."""
        result = reverse_fire_plan(
            current_age=30,
            target_fire_age=50,
            current_assets=100_000,
            annual_expenses=60_000,
        )
        assert result["required_monthly_contribution"] > 0
        assert result["fire_number"] == 1_500_000
        assert result["gap"] > 0
        assert result["years_to_fire"] == 20

    def test_reverse_fire_plan_already_funded(self):
        """Should return 0 contribution when assets already sufficient."""
        result = reverse_fire_plan(
            current_age=30,
            target_fire_age=50,
            current_assets=5_000_000,
            annual_expenses=60_000,
        )
        assert result["required_monthly_contribution"] == 0
        assert result["gap"] == 0

    def test_reverse_fire_plan_invalid_ages(self):
        """target_fire_age <= current_age should raise ValueError."""
        with pytest.raises(ValueError):
            reverse_fire_plan(50, 30, 100_000, 60_000)
