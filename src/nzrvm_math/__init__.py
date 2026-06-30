"""Neutral-Zone Rotational Vector Manifold with Numeric Register Layer.

This package provides mathematical scaffolding for analyzing neutral-zone
rotational systems and translating handwritten numeric registers into
analyzable symbolic objects.

Modules:
    registers: Numeric register analysis and feature extraction.
    neutral_zone: Physics-based scoring for neutral-zone systems.
    matrices: Matrix utilities for handwritten numeric data.
    tokenizer: Tokenization and arrow-chain parsing.

Example:
    >>> from nzrvm_math.registers import analyze_register
    >>> features = analyze_register("76760760716776")
    >>> print(f"Oscillation: {features.oscillation}")
    Oscillation: 43

License:
    GNU Affero General Public License v3.0
    See LICENSE file for details.
"""

__version__ = "2.0.0"
__author__ = "American Eaglestar LLC"
__license__ = "AGPL-3.0"

from .matrices import (
    matrix_from_rows,
    matrix_signature,
    pad_rows,
    parse_number_row,
    row_norm,
)
from .neutral_zone import (
    NeutralZoneResult,
    neutral_stability_score,
    neutral_zone_condition,
    rotational_advantage,
    thrust_from_flow,
    vector_norm,
)
from .registers import (
    RegisterFeatures,
    analyze_register,
    difference_expression,
    digit_frequency,
    digit_vector,
    hamming_distance,
    multiplicity,
    oscillation_score,
    symmetry_score,
    transition_counts,
)
from .tokenizer import (
    TokenizedLine,
    normalize_arrow_text,
    split_arrow_map,
    tokenize_lines,
    tokenize_register,
)

__all__ = [
    "RegisterFeatures",
    "NeutralZoneResult",
    "TokenizedLine",
    "analyze_register",
    "digit_vector",
    "digit_frequency",
    "transition_counts",
    "oscillation_score",
    "symmetry_score",
    "hamming_distance",
    "multiplicity",
    "difference_expression",
    "vector_norm",
    "neutral_stability_score",
    "neutral_zone_condition",
    "rotational_advantage",
    "thrust_from_flow",
    "parse_number_row",
    "pad_rows",
    "matrix_from_rows",
    "row_norm",
    "matrix_signature",
    "tokenize_register",
    "split_arrow_map",
    "normalize_arrow_text",
    "tokenize_lines",
]
