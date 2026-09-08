"""Monte Carlo simulation for FIRE success probability.

Uses geometric Brownian motion for asset returns with inflation-adjusted withdrawals.
"""

from __future__ import annotations
import random
import math
from typing import Dict, Any, Optional


class MonteCarloResult:
    """Structured result from Monte Carlo simulation."""

    def __init__(
        self,
        success_probability: float,
        failure_probability: float,
        median_final_assets: float,
        percentiles: Dict[str, float],
        simulations: int,
        years: int,
    ):
        self.success_probability = success_probability
        self.failure_probability = failure_probability
        self.median_final_assets = median_final_assets
        self.percentiles = percentiles
        self.simulations = simulations
        self.years = years

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success_probability": round(self.success_probability, 4),
            "failure_probability": round(self.failure_probability, 4),
            "success_probability_pct": f"{self.success_probability * 100:.1f}%",
            "failure_probability_pct": f"{self.failure_probability * 100:.1f}%",
            "median_final_assets": round(self.median_final_assets, 2),
            "percentiles": {k: round(v, 2) for k, v in self.percentiles.items()},
            "simulations": self.simulations,
            "years": self.years,
        }


def _single_simulation(
    initial_assets: float,
    annual_withdrawal: float,
    annual_return_mean: float,
    annual_return_volatility: float,
    inflation_rate: float,
    years: int,
) -> float:
    """Run a single Monte Carlo path.

    Args:
        initial_assets: Starting portfolio value.
        annual_withdrawal: First year withdrawal.
        annual_return_mean: Mean annual return.
        annual_return_volatility: Annual return standard deviation.
        inflation_rate: Annual inflation rate.
        years: Simulation duration.

    Returns:
        Final portfolio value (can be negative if depleted).
    """
    assets = initial_assets
    withdrawal = annual_withdrawal

    for _ in range(years):
        # Inflation-adjust withdrawal
        assets -= withdrawal
        if assets <= 0:
            return 0.0

        # Random annual return using log-normal distribution
        # ln(1+r) ~ N(ln(1+mean) - vol^2/2, vol^2)
        log_mean = math.log(1 + annual_return_mean) - 0.5 * annual_return_volatility ** 2
        log_return = random.gauss(log_mean, annual_return_volatility)
        actual_return = math.exp(log_return) - 1

        assets *= (1 + actual_return)
        withdrawal *= (1 + inflation_rate)

    return max(0.0, assets)


def run_monte_carlo(
    initial_assets: float,
    annual_withdrawal: float,
    annual_return: float = 0.07,
    volatility: float = 0.15,
    inflation_rate: float = 0.025,
    years: int = 30,
    simulations: int = 10000,
    seed: Optional[int] = None,
) -> MonteCarloResult:
    """Run Monte Carlo simulation for retirement success.

    Args:
        initial_assets: Starting portfolio value.
        annual_withdrawal: First year withdrawal amount.
        annual_return: Mean annual return.
        volatility: Annual return standard deviation.
        inflation_rate: Annual inflation rate.
        years: Number of years to simulate.
        simulations: Number of Monte Carlo runs.
        seed: Random seed for reproducibility.

    Returns:
        MonteCarloResult with success probability and asset distribution.
    """
    if seed is not None:
        random.seed(seed)

    final_assets_list = []

    for _ in range(simulations):
        final = _single_simulation(
            initial_assets, annual_withdrawal, annual_return,
            volatility, inflation_rate, years
        )
        final_assets_list.append(final)

    final_assets_list.sort()
    n = len(final_assets_list)

    successes = sum(1 for a in final_assets_list if a > 0)
    success_prob = successes / n
    failure_prob = 1 - success_prob

    median_idx = n // 2
    median = final_assets_list[median_idx]

    percentiles = {
        "p10": final_assets_list[int(n * 0.10)],
        "p25": final_assets_list[int(n * 0.25)],
        "p50": final_assets_list[int(n * 0.50)],
        "p75": final_assets_list[int(n * 0.75)],
        "p90": final_assets_list[int(n * 0.90)],
    }

    return MonteCarloResult(
        success_probability=success_prob,
        failure_probability=failure_prob,
        median_final_assets=median,
        percentiles=percentiles,
        simulations=simulations,
        years=years,
    )
