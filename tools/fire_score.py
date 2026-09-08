"""FIRE Readiness Score calculator.

Produces a 0-100 score based on multiple weighted financial dimensions.
All scoring is rule-based and deterministic — no LLM involvement.
"""

from __future__ import annotations
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class DimensionScore:
    name: str
    score: float  # 0-100
    weight: float
    explanation: str


@dataclass
class FireReadinessScore:
    total_score: float
    grade: str
    dimensions: List[DimensionScore]
    summary: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_score": round(self.total_score, 1),
            "grade": self.grade,
            "dimensions": [
                {
                    "name": d.name,
                    "score": round(d.score, 1),
                    "weight": d.weight,
                    "weighted_score": round(d.score * d.weight, 1),
                    "explanation": d.explanation,
                }
                for d in self.dimensions
            ],
            "summary": self.summary,
        }


def _score_asset_coverage(
    current_assets: float,
    fire_number: float,
) -> DimensionScore:
    """Score how well current assets cover the FIRE number."""
    if fire_number <= 0:
        ratio = 1.0
    else:
        ratio = min(current_assets / fire_number, 2.0)

    score = min(ratio * 100, 100)

    if ratio >= 1.0:
        explanation = f"Assets cover {ratio*100:.0f}% of FIRE number. Fully funded."
    elif ratio >= 0.7:
        explanation = f"Assets cover {ratio*100:.0f}% of FIRE number. Close to target."
    elif ratio >= 0.3:
        explanation = f"Assets cover {ratio*100:.0f}% of FIRE number. Significant gap remains."
    else:
        explanation = f"Assets cover only {ratio*100:.0f}% of FIRE number. Early stage."

    return DimensionScore("Asset Coverage", score, 0.25, explanation)


def _score_savings_rate(rate: float) -> DimensionScore:
    """Score based on savings rate."""
    # 0% -> 0, 20% -> 40, 50% -> 75, 70%+ -> 95
    score = min(rate * 130, 95) if rate > 0 else 0

    if rate >= 0.5:
        explanation = f"Savings rate {rate*100:.0f}% is excellent for FIRE."
    elif rate >= 0.3:
        explanation = f"Savings rate {rate*100:.0f}% is good. Further increases accelerate FIRE significantly."
    elif rate >= 0.2:
        explanation = f"Savings rate {rate*100:.0f}% is moderate. Aim for 30%+."
    elif rate > 0:
        explanation = f"Savings rate {rate*100:.0f}% is low. Major improvements needed."
    else:
        explanation = "Negative cash flow. Must fix before FIRE planning."
        score = 0

    return DimensionScore("Savings Rate", score, 0.20, explanation)


def _score_cash_flow(annual_income: float, annual_expenses: float) -> DimensionScore:
    """Score cash flow health."""
    if annual_income <= 0:
        return DimensionScore("Cash Flow", 0, 0.10, "No income reported.")

    ratio = annual_income / annual_expenses if annual_expenses > 0 else 2.0
    score = min(ratio * 40, 100)

    if ratio >= 2.0:
        explanation = "Income is 2x+ expenses. Strong cash flow."
    elif ratio >= 1.5:
        explanation = "Income is 1.5x expenses. Healthy."
    elif ratio >= 1.1:
        explanation = "Income barely exceeds expenses. Tight."
    else:
        explanation = "Expenses close to or exceeding income."
        score = max(score, 10)

    return DimensionScore("Cash Flow", score, 0.10, explanation)


def _score_debt(
    total_debt: float,
    annual_income: float,
) -> DimensionScore:
    """Score debt burden."""
    if annual_income <= 0:
        ratio = 5.0
    else:
        ratio = total_debt / annual_income

    score = max(0, 100 - ratio * 30)

    if ratio == 0:
        explanation = "No debt. Excellent."
    elif ratio < 1:
        explanation = f"Debt-to-income ratio {ratio:.1f}x. Manageable."
    elif ratio < 3:
        explanation = f"Debt-to-income ratio {ratio:.1f}x. Moderate burden."
    else:
        explanation = f"Debt-to-income ratio {ratio:.1f}x. Heavy debt burden."
        score = max(score, 5)

    return DimensionScore("Debt", score, 0.10, explanation)


def _score_emergency_fund(
    cash_assets: float,
    annual_expenses: float,
) -> DimensionScore:
    """Score emergency fund adequacy."""
    if annual_expenses <= 0:
        months = 24
    else:
        months = (cash_assets / annual_expenses) * 12

    score = min(months / 6 * 100, 100)

    if months >= 12:
        explanation = f"Emergency fund covers {months:.0f} months. Very secure."
    elif months >= 6:
        explanation = f"Emergency fund covers {months:.0f} months. Adequate."
    elif months >= 3:
        explanation = f"Emergency fund covers {months:.0f} months. Below recommended."
    else:
        explanation = f"Emergency fund covers only {months:.0f} months. At risk."

    return DimensionScore("Emergency Fund", score, 0.10, explanation)


def _score_portfolio_risk(
    assets: Dict[str, float],
    total_assets: float,
) -> DimensionScore:
    """Score portfolio diversification risk."""
    if total_assets <= 0:
        return DimensionScore("Portfolio Risk", 50, 0.10, "No assets to evaluate.")

    # Check concentration
    max_pct = 0
    asset_types = ["cash", "stocks", "etf", "bonds", "crypto", "real_estate", "other"]
    for atype in asset_types:
        val = assets.get(atype, 0)
        pct = val / total_assets if total_assets > 0 else 0
        max_pct = max(max_pct, pct)

    # Crypto concentration
    crypto_pct = assets.get("crypto", 0) / total_assets if total_assets > 0 else 0

    # Score: lower concentration = higher score
    score = max(0, 100 - max_pct * 100)

    # Penalize heavy crypto
    if crypto_pct > 0.5:
        score *= 0.6
        explanation = f"Heavy crypto concentration ({crypto_pct*100:.0f}%). High volatility risk."
    elif crypto_pct > 0.2:
        score *= 0.8
        explanation = f"Significant crypto allocation ({crypto_pct*100:.0f}%). Consider rebalancing."
    elif max_pct > 0.8:
        explanation = f"Portfolio heavily concentrated ({max_pct*100:.0f}% in one asset type). Diversify."
    elif max_pct > 0.5:
        explanation = f"Some concentration ({max_pct*100:.0f}% in largest holding). Acceptable."
    else:
        explanation = "Well-diversified portfolio."

    return DimensionScore("Portfolio Risk", score, 0.10, explanation)


def _score_time_horizon(
    current_age: int,
    target_fire_age: Optional[int],
) -> DimensionScore:
    """Score based on time remaining to FIRE."""
    if target_fire_age is None:
        years = 20
    else:
        years = max(target_fire_age - current_age, 0)

    # More time = higher score (more room for compounding)
    score = min(years / 30 * 100, 100)

    if years >= 20:
        explanation = f"{years} years to target. Long horizon allows aggressive growth."
    elif years >= 10:
        explanation = f"{years} years to target. Moderate horizon."
    elif years >= 5:
        explanation = f"{years} years to target. Short horizon. Consider more conservative allocation."
    else:
        explanation = f"{years} years to target. Very near-term. High sequence risk."

    return DimensionScore("Time Horizon", score, 0.05, explanation)


def _score_withdrawal_sustainability(
    fire_number: float,
    annual_expenses: float,
    withdrawal_rate: float,
) -> DimensionScore:
    """Score sustainability of withdrawal rate."""
    if withdrawal_rate <= 0:
        return DimensionScore("Withdrawal Sustainability", 50, 0.10, "Default withdrawal rate.")

    # Lower withdrawal rate = more sustainable
    score = max(0, min((0.06 - withdrawal_rate) / 0.04 * 100, 100))

    if withdrawal_rate <= 0.03:
        explanation = f"Withdrawal rate {withdrawal_rate*100:.1f}% is very conservative. Highly sustainable."
    elif withdrawal_rate <= 0.04:
        explanation = f"Withdrawal rate {withdrawal_rate*100:.1f}% is standard. Generally sustainable."
    elif withdrawal_rate <= 0.05:
        explanation = f"Withdrawal rate {withdrawal_rate*100:.1f}% is moderate. Some risk of depletion."
    else:
        explanation = f"Withdrawal rate {withdrawal_rate*100:.1f}% is aggressive. High depletion risk."
        score = max(score, 10)

    return DimensionScore("Withdrawal Sustainability", score, 0.10, explanation)


def calculate_fire_readiness_score(
    current_assets: float,
    fire_number: float,
    annual_income: float,
    annual_expenses: float,
    cash_assets: float,
    total_debt: float,
    assets: Dict[str, float],
    current_age: int,
    target_fire_age: Optional[int] = None,
    withdrawal_rate: float = 0.04,
    savings_rate: float = 0.0,
) -> FireReadinessScore:
    """Calculate comprehensive FIRE readiness score.

    All scoring is deterministic and rule-based.

    Args:
        current_assets: Total investable assets.
        fire_number: Target FIRE number.
        annual_income: Annual income.
        annual_expenses: Annual expenses.
        cash_assets: Cash/savings account balance.
        total_debt: Total debt (mortgage + consumer + other).
        assets: Asset breakdown dict.
        current_age: Current age.
        target_fire_age: Target FIRE age.
        withdrawal_rate: Planned withdrawal rate.
        savings_rate: Current savings rate.

    Returns:
        FireReadinessScore with total score, grade, and dimension breakdown.
    """
    dimensions = [
        _score_asset_coverage(current_assets, fire_number),
        _score_savings_rate(savings_rate),
        _score_cash_flow(annual_income, annual_expenses),
        _score_debt(total_debt, annual_income),
        _score_emergency_fund(cash_assets, annual_expenses),
        _score_portfolio_risk(assets, current_assets),
        _score_time_horizon(current_age, target_fire_age),
        _score_withdrawal_sustainability(fire_number, annual_expenses, withdrawal_rate),
    ]

    total = sum(d.score * d.weight for d in dimensions)

    if total >= 85:
        grade = "A"
    elif total >= 70:
        grade = "B"
    elif total >= 55:
        grade = "C"
    elif total >= 40:
        grade = "D"
    else:
        grade = "F"

    summary_parts = []
    for d in sorted(dimensions, key=lambda x: x.score):
        if d.score < 50:
            summary_parts.append(f"{d.name}: {d.score:.0f}/100")

    if summary_parts:
        summary = f"Areas needing attention: {'; '.join(summary_parts)}."
    else:
        summary = "All dimensions are in good shape."

    return FireReadinessScore(
        total_score=total,
        grade=grade,
        dimensions=dimensions,
        summary=summary,
    )
