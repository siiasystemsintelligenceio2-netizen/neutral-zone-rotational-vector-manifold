# Package: nzrvm_math
# Explicit public API re-exports to avoid accidental API drift.

from __future__ import annotations

# Package metadata (restored to original values)
__version__ = "2.0.0"
__author__ = "American Eaglestar LLC"

# Re-export matrices utilities
from .matrices import (
    parse_number_row,
    pad_rows,
    matrix_from_rows,
    row_norm,
    matrix_signature,
)

# Re-export neutral-zone physics utilities
from .neutral_zone import (
    vector_norm,
    NeutralZoneResult,
    neutral_stability_score,
    neutral_zone_condition,
    rotational_advantage,
    thrust_from_flow,
)

# Re-export register analysis utilities
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

# Re-export tokenizer utilities
from .tokenizer import (
    TokenizedLine,
    tokenize_register,
    split_arrow_map,
    normalize_arrow_text,
    tokenize_lines,
)

# Public API
__all__ = [
    # metadata
    "__version__",
    "__author__",
    # matrices
    "parse_number_row",
    "pad_rows",
    "matrix_from_rows",
    "row_norm",
    "matrix_signature",
    # neutral zone
    "vector_norm",
    "NeutralZoneResult",
    "neutral_stability_score",
    "neutral_zone_condition",
    "rotational_advantage",
    "thrust_from_flow",
    # registers
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
    # tokenizer
    "TokenizedLine",
    "tokenize_register",
    "split_arrow_map",
    "normalize_arrow_text",
    "tokenize_lines",
]
