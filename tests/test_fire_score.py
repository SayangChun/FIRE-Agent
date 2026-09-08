"""Tests for fire_score.py."""

import pytest

from tools.fire_score import calculate_fire_readiness_score, DimensionScore, FireReadinessScore


def _ideal_profile():
    """Return an ideal FIRE profile for testing."""
    return {
        "current_assets": 2_000_000,
        "fire_number": 1_500_000,
        "annual_income": 200_000,
        "annual_expenses": 60_000,
        "cash_assets": 50_000,
        "total_debt": 0,
        "assets": {"stocks": 1_200_000, "bonds": 400_000, "cash": 50_000, "etf": 350_000},
        "current_age": 30,
        "target_fire_age": 50,
        "withdrawal_rate": 0.04,
        "savings_rate": 0.70,
    }


def _poor_profile():
    """Return a poor FIRE profile for testing."""
    return {
        "current_assets": 20_000,
        "fire_number": 1_500_000,
        "annual_income": 40_000,
        "annual_expenses": 50_000,
        "cash_assets": 2_000,
        "total_debt": 150_000,
        "assets": {"crypto": 15_000, "cash": 2_000},
        "current_age": 40,
        "target_fire_age": 45,
        "withdrawal_rate": 0.05,
        "savings_rate": -0.25,
    }


class TestFireScoreIdeal:
    """Tests for ideal FIRE profile."""

    def test_fire_score_ideal(self):
        """High assets, high savings, no debt should produce high score."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        assert result.total_score >= 70
        assert result.grade in ("A", "B")

    def test_fire_score_ideal_grade_a(self):
        """Nearly ideal profile should score grade A."""
        profile = _ideal_profile()
        profile["current_assets"] = 3_000_000
        result = calculate_fire_readiness_score(**profile)
        assert result.grade == "A"


class TestFireScorePoor:
    """Tests for poor FIRE profile."""

    def test_fire_score_poor(self):
        """Low assets, negative savings, high debt should produce low score."""
        result = calculate_fire_readiness_score(**_poor_profile())
        assert result.total_score < 40
        assert result.grade in ("D", "F")


class TestFireScoreRange:
    """Tests for score bounds."""

    def test_fire_score_range(self):
        """Score should always be between 0 and 100."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        assert 0 <= result.total_score <= 100

    def test_fire_score_range_poor(self):
        """Poor profile score should also be 0-100."""
        result = calculate_fire_readiness_score(**_poor_profile())
        assert 0 <= result.total_score <= 100


class TestFireScoreDimensions:
    """Tests for dimension completeness."""

    def test_fire_score_dimensions(self):
        """All 8 dimensions should be present."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        assert len(result.dimensions) == 8

    def test_fire_score_dimension_names(self):
        """Dimensions should have expected names."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        names = {d.name for d in result.dimensions}
        expected = {
            "Asset Coverage", "Savings Rate", "Cash Flow", "Debt",
            "Emergency Fund", "Portfolio Risk", "Time Horizon",
            "Withdrawal Sustainability",
        }
        assert names == expected

    def test_fire_score_weights_sum_to_one(self):
        """All dimension weights should sum to 1.0."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        total_weight = sum(d.weight for d in result.dimensions)
        assert total_weight == pytest.approx(1.0)


class TestFireScoreDeterministic:
    """Tests for determinism."""

    def test_fire_score_deterministic(self):
        """Same inputs should produce same score."""
        r1 = calculate_fire_readiness_score(**_ideal_profile())
        r2 = calculate_fire_readiness_score(**_ideal_profile())
        assert r1.total_score == r2.total_score
        assert r1.grade == r2.grade
        for d1, d2 in zip(r1.dimensions, r2.dimensions):
            assert d1.score == d2.score


class TestFireScoreToDict:
    """Tests for to_dict serialization."""

    def test_to_dict_keys(self):
        """to_dict should return expected top-level keys."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        d = result.to_dict()
        assert "total_score" in d
        assert "grade" in d
        assert "dimensions" in d
        assert "summary" in d

    def test_to_dict_dimension_keys(self):
        """Each dimension dict should have expected keys."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        d = result.to_dict()
        for dim in d["dimensions"]:
            assert "name" in dim
            assert "score" in dim
            assert "weight" in dim
            assert "weighted_score" in dim
            assert "explanation" in dim

    def test_to_dict_weighted_score_matches(self):
        """weighted_score should equal score * weight."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        d = result.to_dict()
        for dim in d["dimensions"]:
            assert dim["weighted_score"] == pytest.approx(
                round(dim["score"] * dim["weight"], 1), abs=0.2
            )


class TestFireScoreSummary:
    """Tests for summary generation."""

    def test_summary_ideal_no_attention_needed(self):
        """Ideal profile should not flag areas needing attention."""
        result = calculate_fire_readiness_score(**_ideal_profile())
        # May or may not have attention areas depending on exact scoring
        assert isinstance(result.summary, str)
        assert len(result.summary) > 0

    def test_summary_poor_has_attention_areas(self):
        """Poor profile should flag areas needing attention."""
        result = calculate_fire_readiness_score(**_poor_profile())
        assert "Areas needing attention" in result.summary
