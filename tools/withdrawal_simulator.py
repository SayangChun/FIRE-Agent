"""Retirement withdrawal simulation.

Simulates asset depletion over time given annual withdrawals and inflation.
"""

from __future__ import annotations
from typing import Dict, Any, List


def simulate_withdrawal(
    initial_assets: float,
    annual_withdrawal: float,
    annual_return: float = 0.04,
    inflation_rate: float = 0.025,
    years: int = 30,
) -> Dict[str, Any]:
    """Simulate retirement withdrawal over N years.

    Withdrawals increase with inflation each year. Assets grow at the
    annual return rate.

    Args:
        initial_assets: Starting portfolio value.
        annual_withdrawal: First year withdrawal amount.
        annual_return: Portfolio annual return rate.
        inflation_rate: Annual inflation rate.
        years: Number of years to simulate.

    Returns:
        Dictionary with remaining_assets, depleted, years_lasted, yearly_series.
    """
    assets = initial_assets
    withdrawal = annual_withdrawal
    depleted = False
    lasted_years = years

    series = []
    for year in range(1, years + 1):
        # Withdrawal at start of year (inflation-adjusted)
        assets -= withdrawal
        if assets < 0:
            series.append({
                "year": year,
                "withdrawal": round(withdrawal, 2),
                "assets_after_withdrawal": 0,
                "assets_after_growth": 0,
                "depleted": True,
            })
            depleted = True
            lasted_years = year - 1 + (assets + withdrawal) / withdrawal if withdrawal > 0 else year - 1
            break

        # Growth for the year
        growth = assets * annual_return
        assets += growth

        series.append({
            "year": year,
            "withdrawal": round(withdrawal, 2),
            "assets_after_withdrawal": round(assets - growth, 2),
            "assets_after_growth": round(assets, 2),
            "depleted": False,
        })

        # Increase withdrawal for inflation
        withdrawal *= (1 + inflation_rate)

    return {
        "initial_assets": initial_assets,
        "final_assets": round(max(0, assets), 2),
        "depleted": depleted,
        "years_lasted": round(lasted_years, 1),
        "total_withdrawn": round(sum(s["withdrawal"] for s in series), 2),
        "yearly_series": series,
    }


def withdrawal_series(
    initial_assets: float,
    annual_withdrawal: float,
    annual_return: float = 0.04,
    inflation_rate: float = 0.025,
    milestones: List[int] | None = None,
) -> List[Dict[str, Any]]:
    """Check remaining assets at specific year milestones.

    Args:
        initial_assets: Starting portfolio value.
        annual_withdrawal: First year withdrawal.
        annual_return: Annual return rate.
        inflation_rate: Annual inflation rate.
        milestones: Years to check. Defaults to [10, 20, 30, 40, 50].

    Returns:
        List of dicts with year and remaining_assets.
    """
    if milestones is None:
        milestones = [10, 20, 30, 40, 50]

    result = simulate_withdrawal(initial_assets, annual_withdrawal, annual_return, inflation_rate, max(milestones))

    series = result["yearly_series"]
    results = []
    for m in milestones:
        entry = next((s for s in series if s["year"] == m), None)
        if entry:
            results.append({
                "year": m,
                "remaining_assets": entry["assets_after_growth"],
                "depleted": entry["depleted"],
            })
        else:
            results.append({
                "year": m,
                "remaining_assets": 0,
                "depleted": True,
            })

    return results
