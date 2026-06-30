"""Matrix utilities for handwritten numeric rows.

This module provides tools for parsing handwritten numeric data into
matrix form and computing matrix signatures.

Example:
    >>> from nzrvm_math.matrices import matrix_from_rows, matrix_signature
    >>> rows = ['13 13 13 25', '209 12.6 6']
    >>> matrix = matrix_from_rows(rows)
    >>> sig = matrix_signature(matrix)
    >>> sig['rows']
    2
"""

from __future__ import annotations

import re
from typing import Iterable, List

NUMBER_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")


def parse_number_row(text: str) -> List[float]:
    """Extract numbers from a text row.
    
    Preserves all numeric values, including negative numbers and decimals.
    Handles various separators (whitespace, commas, etc.).
    
    Args:
        text: String containing numbers separated by non-numeric characters.
        
    Returns:
        List of floats extracted from the text in order of appearance.
        Empty list if no numbers found.
        
    Raises:
        TypeError: If text is not a string.
        
    Examples:
        >>> parse_number_row('13 13 13 25')
        [13.0, 13.0, 13.0, 25.0]
        >>> parse_number_row('209 12.6 6')
        [209.0, 12.6, 6.0]
        >>> parse_number_row('-5 3.14 -2.5')
        [-5.0, 3.14, -2.5]
        >>> parse_number_row('no numbers here')
        []
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return [float(x) for x in NUMBER_PATTERN.findall(text)]


def pad_rows(rows: Iterable[List[float]], fill: float = 0.0) -> List[List[float]]:
    """Pad rows to rectangular matrix form.
    
    Extends shorter rows with fill values to match the longest row.
    Creates a rectangular matrix from jagged input.
    
    Args:
        rows: Iterable of numeric row lists (may have varying lengths).
        fill: Value to use for padding (default 0.0).
        
    Returns:
        List of padded rows forming a rectangular m×n matrix.
        Empty list if input is empty.
        
    Examples:
        >>> pad_rows([[1, 2], [3, 4, 5]])
        [[1.0, 2.0, 0.0], [3.0, 4.0, 5.0]]
        >>> pad_rows([[1]], [[2, 3]])
        [[1.0, 0.0], [2.0, 3.0]]
        >>> pad_rows([], fill=0.0)
        []
    """
    rows_list = [list(row) for row in rows]
    if not rows_list:
        return []
    width = max((len(row) for row in rows_list), default=0)
    return [row + [fill] * (width - len(row)) for row in rows_list]


def matrix_from_rows(text_rows: Iterable[str], fill: float = 0.0) -> List[List[float]]:
    """Convert text rows into a rectangular numeric matrix.
    
    Parses each text row for numeric values and forms a rectangular matrix.
    
    Args:
        text_rows: Iterable of strings containing numeric data.
        fill: Padding value for non-rectangular input (default 0.0).
        
    Returns:
        Rectangular matrix as list of lists of floats.
        Each row guaranteed to have same length.
        
    Examples:
        >>> rows = ['13 13 13 25', '209 12.6 6']
        >>> matrix = matrix_from_rows(rows)
        >>> len(matrix)
        2
        >>> len(matrix[0])
        4
    """
    parsed = [parse_number_row(row) for row in text_rows]
    return pad_rows(parsed, fill=fill)


def row_norm(row: List[float]) -> float:
    """Euclidean norm of a numeric row.
    
    Computes ||row|| = sqrt(sum(x_i^2))
    
    Args:
        row: List of numeric values.
        
    Returns:
        Non-negative Euclidean norm.
        Returns 0.0 for empty row.
        
    Raises:
        TypeError: If row contains non-numeric values.
        
    Examples:
        >>> row_norm([3, 4])
        5.0
        >>> row_norm([0, 0, 0])
        0.0
        >>> row_norm([1, 1, 1])
        1.7320508075688772
    """
    try:
        vals = [float(x) for x in row]
    except (TypeError, ValueError) as e:
        raise TypeError(f"All row values must be numeric: {e}") from e
    return sum(x * x for x in vals) ** 0.5


def matrix_signature(matrix: List[List[float]]) -> dict:
    """Return simple matrix descriptors.
    
    Computes basic properties of a numeric matrix useful for
    characterization and comparison.
    
    Args:
        matrix: 2D list of numeric values (should be rectangular).
        
    Returns:
        Dictionary with keys:
            - 'rows': Number of rows (int)
            - 'cols': Number of columns (int)
            - 'sum': Sum of all elements (float)
            - 'abs_sum': Sum of absolute values (float)
            - 'row_norms': List of Euclidean norms for each row (List[float])
            
    Examples:
        >>> sig = matrix_signature([[1, 2], [3, 4]])
        >>> sig['rows']
        2
        >>> sig['cols']
        2
        >>> round(sig['sum'], 1)
        10.0
        >>> len(sig['row_norms'])
        2
    """
    flat = [x for row in matrix for x in row]
    return {
        "rows": len(matrix),
        "cols": max((len(row) for row in matrix), default=0),
        "sum": sum(flat),
        "abs_sum": sum(abs(x) for x in flat),
        "row_norms": [row_norm(row) for row in matrix],
    }
