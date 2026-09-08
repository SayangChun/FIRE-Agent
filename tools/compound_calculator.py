"""Compound growth calculations.

Implements future value with monthly contributions and inflation adjustment.
"""

from __future__ import annotations
from typing import Dict, Any


def future_value(
    current_assets: float,
    monthly_contribution: float = 0,
    annual_return: float = 0.07,
    years: int = 10,
) -> Dict[str, Any]:
    """Calculate future value of assets with monthly contributions.

    Args:
        current_assets: Starting asset value.
        monthly_contribution: Amount added each month.
        annual_return: Annual return rate (e.g. 0.07 for 7%).
        years: Number of years to project.

    Returns:
        Dictionary with nominal_value, total_contributed, total_growth.
    """
    if annual_return < -1:
        raise ValueError("annual_return must be >= -1")
    if years < 0:
        raise ValueError("years must be >= 0")

    monthly_return = (1 + annual_return) ** (1 / 12) - 1
    months = years * 12

    # Future value of current assets
    fv_current = current_assets * (1 + monthly_return) ** months

    # Future value of monthly contributions (annuity)
    if monthly_return == 0:
        fv_contributions = monthly_contribution * months
    else:
        fv_contributions = monthly_contribution * ((1 + monthly_return) ** months - 1) / monthly_return

    total = fv_current + fv_contributions
    total_contributed = current_assets + monthly_contribution * months
    total_growth = total - total_contributed

    return {
        "nominal_value": round(total, 2),
        "fv_current_assets": round(fv_current, 2),
        "fv_contributions": round(fv_contributions, 2),
        "total_contributed": round(total_contributed, 2),
        "total_growth": round(total_growth, 2),
        "growth_multiple": round(total / total_contributed, 2) if total_contributed > 0 else 0,
    }


def future_value_real(
    current_assets: float,
    monthly_contribution: float = 0,
    annual_return: float = 0.07,
    inflation_rate: float = 0.025,
    years: int = 10,
) -> Dict[str, Any]:
    """Calculate future value adjusted for inflation (real purchasing power).

    Args:
        current_assets: Starting asset value.
        monthly_contribution: Amount added each month.
        annual_return: Annual return rate.
        inflation_rate: Annual inflation rate.
        years: Number of years.

    Returns:
        Dictionary with nominal and real values.
    """
    nominal = future_value(current_assets, monthly_contribution, annual_return, years)

    inflation_factor = (1 + inflation_rate) ** years
    real_value = nominal["nominal_value"] / inflation_factor

    return {
        "nominal_value": nominal["nominal_value"],
        "real_value": round(real_value, 2),
        "inflation_factor": round(inflation_factor, 4),
        "total_contributed": nominal["total_contributed"],
        "real_growth": round(real_value - nominal["total_contributed"], 2),
    }


def compound_growth_series(
    current_assets: float,
    monthly_contribution: float = 0,
    annual_return: float = 0.07,
    years: int = 30,
) -> list[Dict[str, Any]]:
    """Generate year-by-year compound growth series.

    Args:
        current_assets: Starting asset value.
        monthly_contribution: Monthly investment.
        annual_return: Annual return rate.
        years: Total years.

    Returns:
        List of yearly snapshots.
    """
    monthly_return = (1 + annual_return) ** (1 / 12) - 1
    assets = current_assets
    series = []

    for year in range(years + 1):
        if year > 0:
            for _ in range(12):
                assets = assets * (1 + monthly_return) + monthly_contribution
        series.append({
            "year": year,
            "assets": round(assets, 2),
            "contributed": round(current_assets + monthly_contribution * 12 * year, 2),
        })

    return series
