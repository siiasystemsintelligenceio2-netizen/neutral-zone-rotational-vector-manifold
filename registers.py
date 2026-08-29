"""Numeric register analysis for NZ-RVM + NRL-01."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class RegisterFeatures:
    raw: str
    digits: List[int]
    length: int
    digit_sum: int
    frequency: Dict[int, float]
    oscillation: int
    symmetry: float
    transitions: Dict[Tuple[int, int], int]
    multiplicity_6: int


def digit_vector(sequence: str) -> List[int]:
    """Extract all digits as integers from a handwritten sequence."""
    return [int(d) for d in re.findall(r"\d", sequence)]


def digit_frequency(sequence: str) -> Dict[int, float]:
    """Compute digit-frequency distribution for digits 0-9."""
    digits = digit_vector(sequence)
    total = len(digits)
    if total == 0:
        return {k: 0.0 for k in range(10)}
    counts = Counter(digits)
    return {k: counts.get(k, 0) / total for k in range(10)}


def transition_counts(sequence: str) -> Dict[Tuple[int, int], int]:
    """Count adjacent digit transitions."""
    digits = digit_vector(sequence)
    transitions: Counter[Tuple[int, int]] = Counter()
    for a, b in zip(digits, digits[1:]):
        transitions[(a, b)] += 1
    return dict(transitions)


def oscillation_score(sequence: str) -> int:
    """Sum absolute adjacent digit changes."""
    digits = digit_vector(sequence)
    return sum(abs(digits[i + 1] - digits[i]) for i in range(len(digits) - 1))


def hamming_distance(a: List[int], b: List[int]) -> int:
    """Hamming distance for equal-length digit vectors."""
    if len(a) != len(b):
        raise ValueError("Hamming distance requires equal-length lists")
    return sum(x != y for x, y in zip(a, b))


def symmetry_score(sequence: str) -> float:
    """Return mirror symmetry score in [0, 1]."""
    digits = digit_vector(sequence)
    n = len(digits)
    if n == 0:
        return 0.0
    return 1.0 - hamming_distance(digits, list(reversed(digits))) / n


def multiplicity(sequence: str, digit: int = 6) -> int:
    """Count occurrences of a target digit."""
    return digit_vector(sequence).count(digit)


def analyze_register(sequence: str) -> RegisterFeatures:
    """Compute all core features for one register."""
    digits = digit_vector(sequence)
    return RegisterFeatures(
        raw=sequence,
        digits=digits,
        length=len(digits),
        digit_sum=sum(digits),
        frequency=digit_frequency(sequence),
        oscillation=oscillation_score(sequence),
        symmetry=symmetry_score(sequence),
        transitions=transition_counts(sequence),
        multiplicity_6=multiplicity(sequence, 6),
    )


def difference_expression(values: list[float]) -> float:
    """Evaluate a left-associative subtraction chain from numeric values.

    Example: [279, 12.6, 6] -> 260.4
    """
    if not values:
        raise ValueError("difference_expression requires at least one value")
    result = float(values[0])
    for v in values[1:]:
        result -= float(v)
    return result
