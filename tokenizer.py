"""Tokenization utilities for NZ-RVM + NRL-01.

The tokenizer is intentionally conservative. It preserves numbers, decimal fragments,
capital letter runs, arrows, degree symbols, and arithmetic operators.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List

TOKEN_PATTERN = re.compile(r"\d+\.\d+|\d+|[A-Z]+|↔|→|←|=>|>=|<=|>|<|\-|\+|°|\?|\.|/|'")
ARROW_PATTERN = re.compile(r"↔|→|←|=>|->|<-")


@dataclass(frozen=True)
class TokenizedLine:
    raw: str
    tokens: List[str]


def tokenize_register(text: str) -> List[str]:
    """Return a token list from handwritten register text."""
    return TOKEN_PATTERN.findall(text)


def split_arrow_map(text: str) -> List[str]:
    """Split an arrow-chain expression into ordered state labels.

    Examples
    --------
    >>> split_arrow_map("↔24→20→0840→V040")
    ['24', '20', '0840', 'V040']
    """
    cleaned = text.strip().strip('↔')
    parts = [p.strip() for p in ARROW_PATTERN.split(cleaned) if p.strip()]
    return parts


def normalize_arrow_text(text: str) -> str:
    """Normalize common handwritten arrow representations."""
    return text.replace('=>', '→').replace('->', '→').replace('<-', '←')


def tokenize_lines(lines: list[str]) -> list[TokenizedLine]:
    """Tokenize multiple lines."""
    return [TokenizedLine(raw=line, tokens=tokenize_register(line)) for line in lines]
