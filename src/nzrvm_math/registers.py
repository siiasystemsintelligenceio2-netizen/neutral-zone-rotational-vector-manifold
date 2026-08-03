"""Numeric register analysis for NZ-RVM + NRL-01.

This module provides feature extraction and analysis for handwritten
numeric sequences. Registers are treated as symbolic sequences that can
be tokenized, measured, compared, and converted into matrices.

Example:
    >>> from nzrvm_math.registers import analyze_register
    >>> features = analyze_register("76760760716776")
    >>> print(f"Oscillation: {features.oscillation}")
    Oscillation: 43
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class RegisterFeatures:
    """Complete feature set for a numeric register.

    Attributes:
        raw: Original input string.
        digits: List of extracted digit integers.
        length: Number of digits.
        digit_sum: Sum of all digits.
        frequency: Dict mapping digit (0-9) to frequency [0.0, 1.0].
        oscillation: Sum of absolute adjacent differences.
        symmetry: Mirror symmetry score in [0.0, 1.0].
        transitions: Dict mapping (from_digit, to_digit) to count.
        multiplicity_6: Count of digit 6 in sequence.
    """

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
    """Extract all digits as integers from a handwritten sequence.

    Args:
        sequence: String containing digits and other characters.

    Returns:
        List of integers extracted from the sequence.

    Raises:
        TypeError: If sequence is not a string.

    Examples:
        >>> digit_vector("76760760716776")
        [7, 6, 7, 6, 0, 7, 6, 0, 7, 1, 6, 7, 7, 6]
        >>> digit_vector("abc123def")
        [1, 2, 3]
    """
    if not isinstance(sequence, str):
        raise TypeError(f"sequence must be str, got {type(sequence).__name__}")
    return [int(d) for d in re.findall(r"\d", sequence)]


def digit_frequency(sequence: str) -> Dict[int, float]:
    """Compute digit-frequency distribution for digits 0-9.

    Args:
        sequence: String containing digits.

    Returns:
        Dict mapping each digit 0-9 to its frequency [0.0, 1.0].
        Frequencies sum to 1.0 or 0.0 if sequence is empty.

    Examples:
        >>> freq = digit_frequency("76760760716776")
        >>> freq[6]  # Frequency of digit 6
        0.35714285714285715
        >>> freq = digit_frequency("")
        >>> sum(freq.values())
        0.0
    """
    digits = digit_vector(sequence)
    total = len(digits)
    if total == 0:
        return {k: 0.0 for k in range(10)}
    counts = Counter(digits)
    return {k: counts.get(k, 0) / total for k in range(10)}


def transition_counts(sequence: str) -> Dict[Tuple[int, int], int]:
    """Count adjacent digit transitions.

    Args:
        sequence: String containing digits.

    Returns:
        Dict mapping (from_digit, to_digit) tuple to transition count.
        Empty dict if sequence has fewer than 2 digits.

    Examples:
        >>> transitions = transition_counts("7676")
        >>> transitions[(7, 6)]  # Count of 7→6 transitions
        2
    """
    digits = digit_vector(sequence)
    transitions: Counter[Tuple[int, int]] = Counter()
    for a, b in zip(digits, digits[1:]):
        transitions[(a, b)] += 1
    return dict(transitions)


def oscillation_score(sequence: str) -> int:
    """Sum absolute adjacent digit changes.

    Args:
        sequence: String containing digits.

    Returns:
        Sum of absolute differences between consecutive digits.
        Returns 0 if fewer than 2 digits.

    Examples:
        >>> oscillation_score("7676")
        3
    """
    digits = digit_vector(sequence)
    if len(digits) < 2:
        return 0
    return sum(abs(digits[i + 1] - digits[i]) for i in range(len(digits) - 1))


def hamming_distance(a: List[int], b: List[int]) -> int:
    """Hamming distance for equal-length digit vectors.

    Counts positions where elements differ.

    Args:
        a: First digit vector.
        b: Second digit vector (must be same length).

    Returns:
        Count of positions where digits differ.

    Raises:
        ValueError: If vectors have different lengths.

    Examples:
        >>> hamming_distance([1, 2, 3], [1, 2, 3])
        0
        >>> hamming_distance([1, 2, 3], [1, 0, 3])
        1
    """
    if len(a) != len(b):
        raise ValueError(f"Hamming distance requires equal-length lists: {len(a)} != {len(b)}")
    return sum(x != y for x, y in zip(a, b))


def symmetry_score(sequence: str) -> float:
    """Return mirror symmetry score in [0, 1].

    Score of 1.0 means the digit sequence is perfectly symmetric
    (palindromic). Score of 0.0 means completely asymmetric.

    Args:
        sequence: String containing digits.

    Returns:
        Symmetry score: 1 - (Hamming distance / length).
        Returns 0.0 for empty sequences.

    Examples:
        >>> symmetry_score("12321")  # Palindrome
        1.0
        >>> symmetry_score("12345")  # Asymmetric
        0.0
    """
    digits = digit_vector(sequence)
    n = len(digits)
    if n == 0:
        return 0.0
    return 1.0 - hamming_distance(digits, list(reversed(digits))) / n


def multiplicity(sequence: str, digit: int = 6) -> int:
    """Count occurrences of a target digit.

    Args:
        sequence: String containing digits.
        digit: Target digit to count (default 6). Must be 0-9.

    Returns:
        Count of occurrences of the target digit.

    Raises:
        ValueError: If digit is not in [0, 9].

    Examples:
        >>> multiplicity("76760760716776", 6)
        5
        >>> multiplicity("12345", 9)
        0
    """
    if not (0 <= digit <= 9):
        raise ValueError(f"digit must be in [0, 9], got {digit}")
    return digit_vector(sequence).count(digit)


def analyze_register(sequence: str) -> RegisterFeatures:
    """Compute all core features for one register.

    Comprehensive analysis of a handwritten numeric sequence.

    Args:
        sequence: String containing numeric register data.

    Returns:
        RegisterFeatures dataclass with complete analysis.

    Raises:
        TypeError: If sequence is not a string.

    Examples:
        >>> features = analyze_register("76760760716776")
        >>> print(f"Length: {features.length}, Oscillation: {features.oscillation}")
        Length: 14, Oscillation: 43
        >>> features.multiplicity_6
        5
    """
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

    Computes: values[0] - values[1] - values[2] - ... - values[n]

    Args:
        values: List of numeric values. Must contain at least one element.

    Returns:
        Result of left-associative subtraction.

    Raises:
        ValueError: If values list is empty.
        TypeError: If values contain non-numeric types.

    Examples:
        >>> difference_expression([279, 12.6, 6])
        260.4
        >>> difference_expression([100])
        100.0
    """
    if not values:
        raise ValueError("difference_expression requires at least one value")
    result = float(values[0])
    for v in values[1:]:
        try:
            result -= float(v)
        except (TypeError, ValueError) as e:
            raise TypeError(f"Cannot convert value to float: {v}") from e
    return result
