import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nzrvm_math.registers import (  # type: ignore  # noqa: E402
    difference_expression,
    digit_vector,
    oscillation_score,
    symmetry_score,
)
from nzrvm_math.tokenizer import split_arrow_map  # type: ignore  # noqa: E402
from nzrvm_math.neutral_zone import neutral_stability_score, rotational_advantage  # type: ignore  # noqa: E402


def test_digit_vector():
    assert digit_vector("76760760716776") == [7, 6, 7, 6, 0, 7, 6, 0, 7, 1, 6, 7, 7, 6]


def test_arrow_map():
    assert split_arrow_map("↔24→20→0840→V040") == ["24", "20", "0840", "V040"]


def test_difference_expression():
    assert difference_expression([209, 25]) == 184
    assert round(difference_expression([279, 12.6, 6]), 6) == 260.4


def test_scores():
    assert oscillation_score("76760760716776") > 0
    assert 0 <= symmetry_score("76760760716776") <= 1
    sn = neutral_stability_score([0.1, 0.2], [0.05], 1.0, 1.0)
    assert 0 < sn <= 1
    assert rotational_advantage([10, 0], [2, 0], sn) > 0
