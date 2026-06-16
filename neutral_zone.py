"""Neutral-zone physics scoring utilities.

These functions are mathematical scaffolding for bench-scale analysis. They do not
validate propulsion claims by themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Iterable, Sequence


def vector_norm(values: Iterable[float]) -> float:
    """Euclidean norm for a vector-like iterable."""
    vals = list(values)
    return sum(v * v for v in vals) ** 0.5


@dataclass(frozen=True)
class NeutralZoneResult:
    force_norm: float
    torque_norm: float
    force_within_tolerance: bool
    torque_within_tolerance: bool
    stable: bool
    score: float


def neutral_stability_score(
    force_net: Sequence[float] | float,
    torque_net: Sequence[float] | float,
    force_max: float,
    torque_max: float,
) -> float:
    """Compute S_N = exp(-(||F||/Fmax + ||tau||/taumax))."""
    if force_max <= 0 or torque_max <= 0:
        raise ValueError("force_max and torque_max must be positive")
    f_norm = abs(force_net) if isinstance(force_net, (int, float)) else vector_norm(force_net)
    t_norm = abs(torque_net) if isinstance(torque_net, (int, float)) else vector_norm(torque_net)
    return exp(-((f_norm / force_max) + (t_norm / torque_max)))


def neutral_zone_condition(
    force_net: Sequence[float] | float,
    torque_net: Sequence[float] | float,
    force_tolerance: float,
    torque_tolerance: float,
) -> NeutralZoneResult:
    """Evaluate whether force and torque are inside the neutral-zone tolerance."""
    if force_tolerance < 0 or torque_tolerance < 0:
        raise ValueError("tolerances must be non-negative")
    f_norm = abs(force_net) if isinstance(force_net, (int, float)) else vector_norm(force_net)
    t_norm = abs(torque_net) if isinstance(torque_net, (int, float)) else vector_norm(torque_net)
    score = neutral_stability_score(
        f_norm,
        t_norm,
        max(force_tolerance, 1e-12),
        max(torque_tolerance, 1e-12),
    )
    return NeutralZoneResult(
        force_norm=f_norm,
        torque_norm=t_norm,
        force_within_tolerance=f_norm <= force_tolerance,
        torque_within_tolerance=t_norm <= torque_tolerance,
        stable=(f_norm <= force_tolerance and t_norm <= torque_tolerance),
        score=score,
    )


def rotational_advantage(
    output_velocity: Sequence[float] | float,
    input_torque: Sequence[float] | float,
    neutral_score: float,
    epsilon: float = 1e-9,
) -> float:
    """Compute RA = ||V_out|| / (||tau_in|| + epsilon) * S_N."""
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    if neutral_score < 0:
        raise ValueError("neutral_score must be non-negative")
    v_norm = abs(output_velocity) if isinstance(output_velocity, (int, float)) else vector_norm(output_velocity)
    tau_norm = abs(input_torque) if isinstance(input_torque, (int, float)) else vector_norm(input_torque)
    return (v_norm / (tau_norm + epsilon)) * neutral_score


def thrust_from_flow(mass_flow_rate: float, exhaust_velocity: float, pressure_exit: float, pressure_ambient: float, area_exit: float) -> float:
    """Compute F = mdot*v_e + (p_e - p_a)*A_e."""
    return mass_flow_rate * exhaust_velocity + (pressure_exit - pressure_ambient) * area_exit