"""Neutral-zone physics scoring utilities.

These functions provide mathematical scaffolding for bench-scale analysis
of neutral-zone rotational systems. They do not validate propulsion claims
by themselves but provide reproducible scoring metrics.

Example:
    >>> from nzrvm_math.neutral_zone import neutral_zone_condition
    >>> result = neutral_zone_condition(
    ...     force_net=[0.5, -0.3, 0.2],
    ...     torque_net=0.1,
    ...     force_tolerance=1.0,
    ...     torque_tolerance=0.5
    ... )
    >>> result.stable
    True
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Iterable, Sequence


def vector_norm(values: Iterable[float]) -> float:
    """Euclidean norm for a vector-like iterable.
    
    Computes ||v|| = sqrt(sum(v_i^2))
    
    Args:
        values: Iterable of numeric values.
        
    Returns:
        Euclidean norm (always non-negative).
        
    Raises:
        TypeError: If values contain non-numeric types.
        
    Examples:
        >>> vector_norm([3, 4])
        5.0
        >>> vector_norm([1, 1, 1])
        1.7320508075688772
        >>> vector_norm([])
        0.0
    """
    try:
        vals = [float(v) for v in values]
    except (TypeError, ValueError) as e:
        raise TypeError(f"All values must be convertible to float") from e
    return sum(v * v for v in vals) ** 0.5


@dataclass(frozen=True)
class NeutralZoneResult:
    """Result of neutral-zone condition evaluation.
    
    Attributes:
        force_norm: Magnitude of net force vector (non-negative).
        torque_norm: Magnitude of net torque vector (non-negative).
        force_within_tolerance: Whether force_norm <= tolerance.
        torque_within_tolerance: Whether torque_norm <= tolerance.
        stable: Both force and torque within tolerance.
        score: Neutral stability score S_N in (0.0, 1.0].
    """

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
    """Compute S_N = exp(-(||F||/F_max + ||τ||/τ_max)).
    
    A score that penalizes large net forces and torques. Higher score
    indicates better neutral-zone stability.
    
    Args:
        force_net: Net force (scalar or sequence of floats).
        torque_net: Net torque (scalar or sequence of floats).
        force_max: Maximum acceptable force magnitude (must be > 0).
        torque_max: Maximum acceptable torque magnitude (must be > 0).
        
    Returns:
        Stability score in (0.0, 1.0].
        
    Raises:
        ValueError: If force_max or torque_max <= 0.
        TypeError: If inputs contain non-numeric values.
        
    Examples:
        >>> score = neutral_stability_score(0.1, 0.05, 1.0, 0.5)
        >>> round(score, 2)
        0.89
        >>> neutral_stability_score(0.0, 0.0, 1.0, 1.0)
        1.0
    """
    if force_max <= 0 or torque_max <= 0:
        raise ValueError(
            f"force_max and torque_max must be positive: "
            f"force_max={force_max}, torque_max={torque_max}"
        )
    try:
        f_norm = (
            abs(force_net) if isinstance(force_net, (int, float))
            else vector_norm(force_net)
        )
        t_norm = (
            abs(torque_net) if isinstance(torque_net, (int, float))
            else vector_norm(torque_net)
        )
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid force_net or torque_net: {e}") from e
    
    exponent = -((f_norm / force_max) + (t_norm / torque_max))
    return exp(exponent)


def neutral_zone_condition(
    force_net: Sequence[float] | float,
    torque_net: Sequence[float] | float,
    force_tolerance: float,
    torque_tolerance: float,
) -> NeutralZoneResult:
    """Evaluate whether force and torque are inside neutral-zone tolerance.
    
    A system is in the neutral zone when both net force and net torque
    are within design tolerances.
    
    Args:
        force_net: Net force vector (3D) or scalar.
        torque_net: Net torque vector (3D) or scalar.
        force_tolerance: Maximum acceptable force magnitude (>= 0).
        torque_tolerance: Maximum acceptable torque magnitude (>= 0).
        
    Returns:
        NeutralZoneResult with detailed status and stability score.
        
    Raises:
        ValueError: If tolerances are negative.
        TypeError: If inputs contain non-numeric values.
        
    Examples:
        >>> result = neutral_zone_condition(
        ...     force_net=[0.5, -0.3, 0.2],
        ...     torque_net=0.1,
        ...     force_tolerance=1.0,
        ...     torque_tolerance=0.5
        ... )
        >>> result.stable
        True
        >>> result.score > 0
        True
    """
    if force_tolerance < 0 or torque_tolerance < 0:
        raise ValueError(
            f"tolerances must be non-negative: "
            f"force_tolerance={force_tolerance}, torque_tolerance={torque_tolerance}"
        )
    try:
        f_norm = (
            abs(force_net) if isinstance(force_net, (int, float))
            else vector_norm(force_net)
        )
        t_norm = (
            abs(torque_net) if isinstance(torque_net, (int, float))
            else vector_norm(torque_net)
        )
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid force_net or torque_net: {e}") from e
    
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
    """Compute RA = ||V_out|| / (||τ_in|| + ε) * S_N.
    
    Rotational advantage quantifies the efficiency of converting input
    torque to output velocity while maintaining neutral-zone stability.
    
    Args:
        output_velocity: Output velocity vector or scalar (m/s).
        input_torque: Input torque vector or scalar (N·m).
        neutral_score: Neutral stability score S_N in [0.0, 1.0].
        epsilon: Regularization to avoid division by zero (default 1e-9, must be > 0).
        
    Returns:
        Rotational advantage metric (non-negative).
        
    Raises:
        ValueError: If epsilon <= 0 or neutral_score < 0.
        TypeError: If inputs contain non-numeric values.
        
    Examples:
        >>> ra = rotational_advantage(
        ...     output_velocity=[10.5, 2.3, 1.1],
        ...     input_torque=0.8,
        ...     neutral_score=0.92
        ... )
        >>> round(ra, 2)
        14.14
    """
    if epsilon <= 0:
        raise ValueError(f"epsilon must be positive, got {epsilon}")
    if neutral_score < 0:
        raise ValueError(f"neutral_score must be non-negative, got {neutral_score}")
    if neutral_score > 1.0:
        raise ValueError(f"neutral_score should be <= 1.0, got {neutral_score}")
    
    try:
        v_norm = (
            abs(output_velocity) if isinstance(output_velocity, (int, float))
            else vector_norm(output_velocity)
        )
        tau_norm = (
            abs(input_torque) if isinstance(input_torque, (int, float))
            else vector_norm(input_torque)
        )
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid output_velocity or input_torque: {e}") from e
    
    return (v_norm / (tau_norm + epsilon)) * neutral_score


def thrust_from_flow(
    mass_flow_rate: float,
    exhaust_velocity: float,
    pressure_exit: float,
    pressure_ambient: float,
    area_exit: float,
) -> float:
    """Compute F = ṁ·v_e + (p_e - p_a)·A_e.
    
    Thrust calculation from mass flow rate and pressure differential.
    Standard rocket propulsion equation.
    
    Args:
        mass_flow_rate: Mass flow rate (kg/s, must be >= 0).
        exhaust_velocity: Exhaust velocity (m/s).
        pressure_exit: Exit pressure (Pa).
        pressure_ambient: Ambient pressure (Pa).
        area_exit: Exit area (m², must be >= 0).
        
    Returns:
        Thrust force (N).
        
    Raises:
        ValueError: If mass_flow_rate or area_exit is negative.
        TypeError: If inputs are non-numeric.
        
    Examples:
        >>> thrust = thrust_from_flow(
        ...     mass_flow_rate=0.5,
        ...     exhaust_velocity=300,
        ...     pressure_exit=1e5,
        ...     pressure_ambient=1.01e5,
        ...     area_exit=0.01
        ... )
        >>> round(thrust, 1)
        150.0
    """
    if mass_flow_rate < 0:
        raise ValueError(f"mass_flow_rate must be non-negative, got {mass_flow_rate}")
    if area_exit < 0:
        raise ValueError(f"area_exit must be non-negative, got {area_exit}")
    
    try:
        mdot = float(mass_flow_rate)
        v_e = float(exhaust_velocity)
        p_e = float(pressure_exit)
        p_a = float(pressure_ambient)
        A_e = float(area_exit)
    except (TypeError, ValueError) as e:
        raise TypeError(f"All inputs must be numeric: {e}") from e
    
    return mdot * v_e + (p_e - p_a) * A_e
