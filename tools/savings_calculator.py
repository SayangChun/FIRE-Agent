"""Savings rate calculations.

Formulas:
    Annual Savings = Annual Income - Annual Expenses
    Savings Rate = Annual Savings / Annual Income
"""

from __future__ import annotations
from typing import Dict, Any


def annual_savings(annual_income: float, annual_expenses: float) -> float:
    """Calculate annual savings.

    Args:
        annual_income: Total annual income before taxes.
        annual_expenses: Total annual expenses.

    Returns:
        Annual savings amount (can be negative if expenses > income).
    """
    return annual_income - annual_expenses


def calculate_savings_rate(
    annual_income: float,
    annual_expenses: float,
) -> Dict[str, Any]:
    """Calculate savings rate with validation and diagnostics.

    Args:
        annual_income: Total annual income before taxes.
        annual_expenses: Total annual expenses.

    Returns:
        Dictionary with savings_rate, annual_savings, diagnostics.
    """
    if annual_income < 0:
        raise ValueError("annual_income must be >= 0")

    savings = annual_savings(annual_income, annual_expenses)
    rate = savings / annual_income if annual_income > 0 else 0.0

    diagnostics = []
    if savings < 0:
        diagnostics.append("WARNING: Cash flow is negative. Prioritize fixing cash flow before FIRE planning.")
    elif rate < 0.2:
        diagnostics.append("Savings rate below 20%. Consider increasing income or reducing expenses.")
    elif rate < 0.5:
        diagnostics.append("Moderate savings rate. Increasing to 50%+ significantly accelerates FIRE.")
    else:
        diagnostics.append("Excellent savings rate. Well positioned for FIRE.")

    return {
        "savings_rate": round(rate, 6),
        "savings_rate_pct": f"{rate * 100:.1f}%",
        "annual_savings": round(savings, 2),
        "annual_income": annual_income,
        "annual_expenses": annual_expenses,
        "monthly_savings": round(savings / 12, 2),
        "diagnostics": diagnostics,
    }


def savings_rate_sensitivity(
    annual_income: float,
    annual_expenses: float,
    target_rates: list[float] | None = None,
) -> list[Dict[str, Any]]:
    """Show how different savings rates affect the required expenses.

    Args:
        annual_income: Annual income.
        annual_expenses: Current annual expenses.
        target_rates: Target savings rates to analyze.

    Returns:
        List of dicts showing required expenses and savings for each target rate.
    """
    if target_rates is None:
        target_rates = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    results = []
    for rate in target_rates:
        required_savings = annual_income * rate
        required_expenses = annual_income - required_savings
        results.append({
            "target_rate": rate,
            "target_rate_pct": f"{rate * 100:.0f}%",
            "required_annual_expenses": round(required_expenses, 2),
            "required_annual_savings": round(required_savings, 2),
            "expense_reduction_needed": round(max(0, annual_expenses - required_expenses), 2),
        })
    return results
