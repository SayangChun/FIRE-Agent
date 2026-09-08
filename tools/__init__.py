"""FIRE Agent calculation tools."""

from .fire_calculator import calculate_fire_number, calculate_fire_progress, estimate_fire_age
from .savings_calculator import calculate_savings_rate, annual_savings
from .compound_calculator import future_value, future_value_real
from .withdrawal_simulator import simulate_withdrawal, withdrawal_series
from .monte_carlo import run_monte_carlo, MonteCarloResult
from .fire_score import calculate_fire_readiness_score, FireReadinessScore

__all__ = [
    "calculate_fire_number",
    "calculate_fire_progress",
    "estimate_fire_age",
    "calculate_savings_rate",
    "annual_savings",
    "future_value",
    "future_value_real",
    "simulate_withdrawal",
    "withdrawal_series",
    "run_monte_carlo",
    "MonteCarloResult",
    "calculate_fire_readiness_score",
    "FireReadinessScore",
]
