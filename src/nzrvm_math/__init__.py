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
    parse_number_row,
    pad_rows,
    matrix_from_rows,
    row_norm,
    matrix_signature,
)

from .neutral_zone import (
    vector_norm,
    NeutralZoneResult,
    neutral_stability_score,
    neutral_zone_condition,
    rotational_advantage,
    thrust_from_flow,
)

from .registers import (
    RegisterFeatures,
    digit_vector,
    digit_frequency,
    transition_counts,
    oscillation_score,
    hamming_distance,
    symmetry_score,
    multiplicity,
    analyze_register,
    difference_expression,
)

from .tokenizer import (
    TokenizedLine,
    tokenize_register,
    split_arrow_map,
    normalize_arrow_text,
    tokenize_lines,
)

__all__ = [
    "__version__",
    "__author__",
    "parse_number_row",
    "pad_rows",
    "matrix_from_rows",
    "row_norm",
    "matrix_signature",
    "vector_norm",
    "NeutralZoneResult",
    "neutral_stability_score",
    "neutral_zone_condition",
    "rotational_advantage",
    "thrust_from_flow",
    "RegisterFeatures",
    "digit_vector",
    "digit_frequency",
    "transition_counts",
    "oscillation_score",
    "hamming_distance",
    "symmetry_score",
    "multiplicity",
    "analyze_register",
    "difference_expression",
    "TokenizedLine",
    "tokenize_register",
    "split_arrow_map",
    "normalize_arrow_text",
    "tokenize_lines",
]
