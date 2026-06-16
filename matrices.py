"""Matrix helpers for handwritten numeric rows."""

from __future__ import annotations

import re
from typing import Iterable, List

NUMBER_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")


def parse_number_row(text: str) -> List[float]:
    """Extract numbers from a row.

    This keeps all numeric values, including values inside subtraction fragments.
    For example, '13 13 13 25 209-25' -> [13, 13, 13, 25, 209, -25]
    """
    return [float(x) for x in NUMBER_PATTERN.findall(text)]


def pad_rows(rows: Iterable[List[float]], fill: float = 0.0) -> List[List[float]]:
    """Pad rows to rectangular matrix form."""
    rows = [list(row) for row in rows]
    width = max((len(row) for row in rows), default=0)
    return [row + [fill] * (width - len(row)) for row in rows]


def matrix_from_rows(text_rows: Iterable[str], fill: float = 0.0) -> List[List[float]]:
    """Convert text rows into a rectangular numeric matrix."""
    parsed = [parse_number_row(row) for row in text_rows]
    return pad_rows(parsed, fill=fill)


def row_norm(row: List[float]) -> float:
    """Euclidean norm of a numeric row."""
    return sum(x * x for x in row) ** 0.5


def matrix_signature(matrix: List[List[float]]) -> dict:
    """Return simple matrix descriptors."""
    flat = [x for row in matrix for x in row]
    return {
        "rows": len(matrix),
        "cols": max((len(row) for row in matrix), default=0),
        "sum": sum(flat),
        "abs_sum": sum(abs(x) for x in flat),
        "row_norms": [row_norm(row) for row in matrix],
    }