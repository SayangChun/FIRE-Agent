"""FIRE Number and related calculations.

Formulas:
    FIRE Number = Annual Retirement Expenses / Withdrawal Rate
    FIRE Progress = Investable Assets / FIRE Number
    FIRE Age = solve for years where compound(assets, contribution, return) >= FIRE Number
"""

from __future__ import annotations
from typing import List, Dict, Any


def calculate_fire_number(
    annual_retirement_expenses: float,
    withdrawal_rate: float = 0.04,
) -> Dict[str, Any]:
    """Calculate the FIRE number for a given withdrawal rate.

    Args:
        annual_retirement_expenses: Expected annual spending in retirement.
        withdrawal_rate: Safe withdrawal rate (e.g. 0.04 for 4%).

    Returns:
        Dictionary with fire_number, withdrawal_rate, annual_expenses.

    Raises:
        ValueError: If withdrawal_rate <= 0 or annual_retirement_expenses < 0.
    """
    if withdrawal_rate <= 0:
        raise ValueError("withdrawal_rate must be > 0")
    if annual_retirement_expenses < 0:
        raise ValueError("annual_retirement_expenses must be >= 0")

    fire_number = annual_retirement_expenses / withdrawal_rate
    return {
        "fire_number": round(fire_number, 2),
        "withdrawal_rate": withdrawal_rate,
        "annual_retirement_expenses": annual_retirement_expenses,
    }


def fire_number_sensitivity(
    annual_retirement_expenses: float,
    rates: List[float] | None = None,
) -> List[Dict[str, Any]]:
    """Calculate FIRE number across multiple withdrawal rates.

    Args:
        annual_retirement_expenses: Expected annual spending in retirement.
        rates: List of withdrawal rates. Defaults to [0.025, 0.03, 0.035, 0.04, 0.045, 0.05].

    Returns:
        List of dicts with rate and fire_number.
    """
    if rates is None:
        rates = [0.025, 0.03, 0.035, 0.04, 0.045, 0.05]

    results = []
    for rate in rates:
        result = calculate_fire_number(annual_retirement_expenses, rate)
        results.append({
            "withdrawal_rate": rate,
            "withdrawal_rate_pct": f"{rate * 100:.1f}%",
            "fire_number": result["fire_number"],
        })
    return results


def calculate_fire_progress(
    current_investable_assets: float,
    fire_number: float,
) -> Dict[str, Any]:
    """Calculate progress toward FIRE.

    Args:
        current_investable_assets: Total investable assets (excludes primary residence by default).
        fire_number: Target FIRE number.

    Returns:
        Dictionary with progress percentage, remaining amount, current_assets, fire_number.
    """
    if fire_number <= 0:
        raise ValueError("fire_number must be > 0")

    progress = current_investable_assets / fire_number
    remaining = max(0, fire_number - current_investable_assets)

    return {
        "current_assets": current_investable_assets,
        "fire_number": fire_number,
        "progress": round(progress, 6),
        "progress_pct": f"{progress * 100:.1f}%",
        "remaining": round(remaining, 2),
        "remaining_pct": f"{max(0, 1 - progress) * 100:.1f}%",
    }


def estimate_fire_age(
    current_age: int,
    current_assets: float,
    monthly_contribution: float,
    annual_return: float,
    fire_number: float,
    inflation_rate: float = 0.025,
) -> Dict[str, Any]:
    """Estimate the age at which FIRE is reached using compound growth.

    Uses iterative year-by-year simulation rather than closed-form to handle
    monthly contributions accurately.

    Args:
        current_age: Current age.
        current_assets: Current investable assets.
        monthly_contribution: Amount invested per month.
        annual_return: Expected annual return rate (e.g. 0.07 for 7%).
        fire_number: Target FIRE number.
        inflation_rate: Annual inflation rate.

    Returns:
        Dictionary with estimated_fire_age, estimated_fire_year, years_remaining,
        nominal_assets, real_assets.
    """
    if fire_number <= 0:
        raise ValueError("fire_number must be > 0")
    if annual_return < -1:
        raise ValueError("annual_return must be >= -1")

    monthly_return = (1 + annual_return) ** (1 / 12) - 1
    monthly_inflation = (1 + inflation_rate) ** (1 / 12) - 1

    assets = current_assets
    years = 0
    max_years = 100

    while assets < fire_number and years < max_years:
        for _ in range(12):
            assets = assets * (1 + monthly_return) + monthly_contribution
        years += 1

    real_assets = assets / ((1 + inflation_rate) ** years) if years > 0 else assets

    fire_age = current_age + years if years < max_years else None
    reached = years < max_years

    return {
        "reached": reached,
        "estimated_fire_age": fire_age,
        "years_remaining": years if reached else None,
        "nominal_assets": round(assets, 2),
        "real_assets": round(real_assets, 2),
        "fire_number_nominal": fire_number,
    }


def reverse_fire_plan(
    current_age: int,
    target_fire_age: int,
    current_assets: float,
    annual_expenses: float,
    withdrawal_rate: float = 0.04,
    annual_return: float = 0.07,
) -> Dict[str, Any]:
    """Calculate required monthly contribution to reach FIRE by target age.

    Args:
        current_age: Current age.
        target_fire_age: Desired FIRE age.
        current_assets: Current investable assets.
        annual_expenses: Expected annual retirement expenses.
        withdrawal_rate: Safe withdrawal rate.
        annual_return: Expected annual return.

    Returns:
        Dictionary with required_monthly_contribution and other details.
    """
    years = target_fire_age - current_age
    if years <= 0:
        raise ValueError("target_fire_age must be > current_age")

    fire_number = annual_expenses / withdrawal_rate
    monthly_return = (1 + annual_return) ** (1 / 12) - 1
    months = years * 12

    # Future value of current assets
    fv_current = current_assets * (1 + monthly_return) ** months

    # Required future value from contributions
    gap = fire_number - fv_current

    if gap <= 0:
        return {
            "required_monthly_contribution": 0,
            "fire_number": round(fire_number, 2),
            "gap": 0,
            "message": "Current assets already exceed FIRE number at target age.",
        }

    # FV of annuity formula: PMT * ((1+r)^n - 1) / r
    if monthly_return == 0:
        monthly_contribution = gap / months
    else:
        monthly_contribution = gap * monthly_return / ((1 + monthly_return) ** months - 1)

    return {
        "required_monthly_contribution": round(monthly_contribution, 2),
        "fire_number": round(fire_number, 2),
        "gap": round(gap, 2),
        "years_to_fire": years,
        "current_assets": current_assets,
        "target_fire_age": target_fire_age,
    }
