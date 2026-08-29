"""Tokenization utilities for NZ-RVM + NRL-01.

The tokenizer is intentionally conservative, preserving numbers,
decimal fragments, capital letter runs, arrows, and operators.

Example:
    >>> from nzrvm_math.tokenizer import split_arrow_map, tokenize_register
    >>> split_arrow_map("↔24→20→0840→V040")
    ['24', '20', '0840', 'V040']
    >>> tokenize_register("↔24→20→0840→V040")
    ['↔', '24', '→', '20', '→', '0840', '→', 'V', '040']
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List

TOKEN_PATTERN = re.compile(
    r"\d+\.\d+|\d+|[A-Z]+|\u2194|\u2192|\u2190|=>|>=|<=|>|<|\-|\+|\u00b0|\?|\.|/|'"
)
ARROW_PATTERN = re.compile(r"\u2194|\u2192|\u2190|=>|->|<-")


@dataclass(frozen=True)
class TokenizedLine:
    """Result of tokenizing a single line.

    Attributes:
        raw: Original input line (unmodified).
        tokens: List of extracted tokens in order of appearance.
    """

    raw: str
    tokens: List[str]


def tokenize_register(text: str) -> List[str]:
    """Return a token list from handwritten register text.

    Extracts: numbers (including decimals), capital letter runs, arrows,
    and mathematical operators. Preserves order.

    Args:
        text: Input string with mixed content (numbers, letters, symbols).

    Returns:
        List of tokens extracted from the text in order.
        Empty list if no tokens found.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> tokenize_register("↔24→20→0840→V040")
        ['↔', '24', '→', '20', '→', '0840', '→', 'V', '040']
        >>> tokenize_register("12.5 ABC >= 3")
        ['12.5', 'ABC', '>=', '3']
        >>> tokenize_register(".,.")
        ['.', '.']  # Periods are tokens
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return TOKEN_PATTERN.findall(text)


def split_arrow_map(text: str) -> List[str]:
    """Split an arrow-chain expression into ordered state labels.

    Extracts state names from arrow chains, handling bidirectional
    (↔), forward (→), and backward (←) arrow notation.
    Strips leading/trailing bidirectional arrows.

    Args:
        text: String containing arrow-separated states.

    Returns:
        List of state labels (stripped of whitespace) in order.
        Empty list if no states found.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> split_arrow_map("↔24→20→0840→V040")
        ['24', '20', '0840', 'V040']
        >>> split_arrow_map("A → B ← C")
        ['A', 'B', 'C']
        >>> split_arrow_map("↔start↔")
        ['start']
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    cleaned = text.strip().strip("↔")
    parts = [p.strip() for p in ARROW_PATTERN.split(cleaned) if p.strip()]
    return parts


def normalize_arrow_text(text: str) -> str:
    """Normalize common handwritten arrow representations to Unicode.

    Converts various arrow notations to standard Unicode arrows:
    - '=>' → '→' (forward)
    - '->' → '→' (forward)
    - '<-' → '←' (backward)

    Args:
        text: String with mixed arrow notations.

    Returns:
        String with normalized arrows.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> normalize_arrow_text("A => B -> C")
        'A → B → C'
        >>> normalize_arrow_text("X <- Y")
        'X ← Y'
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return text.replace("=>", "→").replace("->", "→").replace("<-", "←")


def tokenize_lines(lines: list[str]) -> list[TokenizedLine]:
    """Tokenize multiple lines.

    Applies tokenization to each input line independently.

    Args:
        lines: List of input strings to tokenize.

    Returns:
        List of TokenizedLine objects, one per input line.

    Raises:
        TypeError: If lines is not a list or contains non-strings.

    Examples:
        >>> lines = ["↔24→20", "76760760716776"]
        >>> results = tokenize_lines(lines)
        >>> len(results)
        2
        >>> results[0].raw
        '↔24→20'
        >>> len(results[0].tokens)
        5  # ['↔', '24', '→', '20']
    """
    if not isinstance(lines, list):
        raise TypeError(f"lines must be list, got {type(lines).__name__}")
    return [
        TokenizedLine(raw=line, tokens=tokenize_register(line))
        for line in lines
    ]
