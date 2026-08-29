"""Unit tests for NZ-RVM core modules."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))  # noqa: E402

from nzrvm_math.registers import (  # type: ignore  # noqa: E402
    analyze_register,
    digit_frequency,
    digit_vector,
    difference_expression,
    hamming_distance,
    multiplicity,
    oscillation_score,
    symmetry_score,
    transition_counts,
)
from nzrvm_math.tokenizer import split_arrow_map  # type: ignore  # noqa: E402
from nzrvm_math.neutral_zone import (  # type: ignore  # noqa: E402
    neutral_stability_score,
    neutral_zone_condition,
    rotational_advantage,
)
from nzrvm_math.matrices import (  # type: ignore  # noqa: E402
    matrix_from_rows,
    matrix_signature,
    parse_number_row,
    pad_rows,
    row_norm,
)


# ============================================================================
# Test: digit_vector
# ============================================================================


def test_digit_vector_basic():
    """Test basic digit extraction."""
    assert digit_vector("76760760716776") == [7, 6, 7, 6, 0, 7, 6, 0, 7, 1, 6, 7, 7, 6]


def test_digit_vector_with_text():
    """Test digit extraction from mixed alphanumeric."""
    assert digit_vector("abc123def456") == [1, 2, 3, 4, 5, 6]


def test_digit_vector_empty():
    """Test empty sequence returns empty list."""
    assert digit_vector("") == []
    assert digit_vector("abc") == []


def test_digit_vector_single_digit():
    """Test single digit."""
    assert digit_vector("5") == [5]


def test_digit_vector_all_same():
    """Test sequence with all identical digits."""
    assert digit_vector("7777777") == [7, 7, 7, 7, 7, 7, 7]


def test_digit_vector_invalid_type():
    """Test TypeError on non-string input."""
    with pytest.raises(TypeError):
        digit_vector(12345)


# ============================================================================
# Test: digit_frequency
# ============================================================================


def test_digit_frequency_basic():
    """Test frequency computation."""
    freq = digit_frequency("76760760716776")
    assert freq[6] == pytest.approx(5 / 14)
    assert freq[7] == pytest.approx(5 / 14)
    assert freq[0] == pytest.approx(2 / 14)
    assert freq[1] == pytest.approx(1 / 14)


def test_digit_frequency_empty():
    """Test empty sequence returns zeros."""
    freq = digit_frequency("")
    assert all(v == 0.0 for v in freq.values())
    assert sum(freq.values()) == 0.0


def test_digit_frequency_all_same():
    """Test sequence with single digit value."""
    freq = digit_frequency("5555")
    assert freq[5] == 1.0
    assert all(v == 0.0 for k, v in freq.items() if k != 5)


def test_digit_frequency_sums_to_one():
    """Test that frequencies sum to 1.0 (or 0.0 if empty)."""
    freq = digit_frequency("123456789012345")
    assert sum(freq.values()) == pytest.approx(1.0)


# ============================================================================
# Test: oscillation_score
# ============================================================================


def test_oscillation_score_basic():
    """Test oscillation (sum of absolute differences)."""
    # "7676": |7-6| + |6-7| + |7-6| = 1 + 1 + 1 = 3
    assert oscillation_score("7676") == 3


def test_oscillation_score_empty():
    """Test empty or single-digit returns 0."""
    assert oscillation_score("") == 0
    assert oscillation_score("5") == 0


def test_oscillation_score_no_change():
    """Test sequence with no changes."""
    assert oscillation_score("5555") == 0


def test_oscillation_score_high_variance():
    """Test sequence with large changes."""
    # "09": |0-9| = 9
    assert oscillation_score("09") == 9


# ============================================================================
# Test: symmetry_score
# ============================================================================


def test_symmetry_score_palindrome():
    """Test perfect palindrome."""
    assert symmetry_score("12321") == 1.0


def test_symmetry_score_asymmetric():
    """Test completely asymmetric sequence."""
    assert symmetry_score("12345") == 0.0


def test_symmetry_score_empty():
    """Test empty returns 0.0."""
    assert symmetry_score("") == 0.0


def test_symmetry_score_single():
    """Test single digit (palindrome)."""
    assert symmetry_score("5") == 1.0


def test_symmetry_score_partial():
    """Test partially symmetric sequence."""
    # "121": reverse is "121", Hamming distance 0, symmetry = 1.0
    assert symmetry_score("121") == 1.0
    # "1231": reverse is "1321", Hamming distance 2/4 = 0.5
    assert symmetry_score("1231") == pytest.approx(0.5)


# ============================================================================
# Test: transition_counts
# ============================================================================


def test_transition_counts_basic():
    """Test transition counting."""
    trans = transition_counts("7676")
    assert trans[(7, 6)] == 2
    assert trans[(6, 7)] == 1


def test_transition_counts_empty():
    """Test empty or single digit returns empty dict."""
    assert transition_counts("") == {}
    assert transition_counts("5") == {}


def test_transition_counts_all_same():
    """Test all same digit (no transitions)."""
    assert transition_counts("5555") == {}


def test_transition_counts_repeated():
    """Test repeated transitions."""
    trans = transition_counts("123123")
    assert trans[(1, 2)] == 2
    assert trans[(2, 3)] == 2
    assert trans[(3, 1)] == 1


# ============================================================================
# Test: multiplicity
# ============================================================================


def test_multiplicity_basic():
    """Test digit counting."""
    assert multiplicity("76760760716776", 6) == 5
    assert multiplicity("76760760716776", 7) == 5


def test_multiplicity_none():
    """Test digit not present."""
    assert multiplicity("12345", 9) == 0


def test_multiplicity_all():
    """Test all same digit."""
    assert multiplicity("5555", 5) == 4


def test_multiplicity_invalid_digit():
    """Test invalid digit raises ValueError."""
    with pytest.raises(ValueError):
        multiplicity("123", 10)
    with pytest.raises(ValueError):
        multiplicity("123", -1)


# ============================================================================
# Test: hamming_distance
# ============================================================================


def test_hamming_distance_identical():
    """Test identical sequences."""
    assert hamming_distance([1, 2, 3], [1, 2, 3]) == 0


def test_hamming_distance_single_diff():
    """Test single difference."""
    assert hamming_distance([1, 2, 3], [1, 0, 3]) == 1


def test_hamming_distance_all_diff():
    """Test all differences."""
    assert hamming_distance([1, 2, 3], [4, 5, 6]) == 3


def test_hamming_distance_length_mismatch():
    """Test unequal length raises ValueError."""
    with pytest.raises(ValueError):
        hamming_distance([1, 2], [1, 2, 3])


# ============================================================================
# Test: analyze_register
# ============================================================================


def test_analyze_register_comprehensive():
    """Test complete register analysis."""
    features = analyze_register("76760760716776")
    
    assert features.raw == "76760760716776"
    assert features.digits == [7, 6, 7, 6, 0, 7, 6, 0, 7, 1, 6, 7, 7, 6]
    assert features.length == 14
    assert features.digit_sum == sum(features.digits)
    assert features.oscillation > 0
    assert 0 <= features.symmetry <= 1
    assert features.multiplicity_6 == 5
    assert len(features.frequency) == 10
    assert len(features.transitions) > 0


def test_analyze_register_empty():
    """Test empty register."""
    features = analyze_register("")
    assert features.length == 0
    assert features.digit_sum == 0
    assert features.oscillation == 0
    assert features.symmetry == 0.0
    assert features.multiplicity_6 == 0


def test_analyze_register_single():
    """Test single-digit register."""
    features = analyze_register("5")
    assert features.length == 1
    assert features.digit_sum == 5
    assert features.oscillation == 0
    assert features.symmetry == 1.0
    assert features.multiplicity_6 == 0


# ============================================================================
# Test: difference_expression
# ============================================================================


def test_difference_expression_basic():
    """Test basic subtraction chain."""
    assert difference_expression([209, 25]) == 184


def test_difference_expression_floats():
    """Test with floating point values."""
    assert round(difference_expression([279, 12.6, 6]), 6) == 260.4


def test_difference_expression_single():
    """Test single value returns itself."""
    assert difference_expression([100]) == 100.0


def test_difference_expression_empty():
    """Test empty list raises ValueError."""
    with pytest.raises(ValueError):
        difference_expression([])


def test_difference_expression_negative_result():
    """Test that result can be negative."""
    assert difference_expression([10, 20, 5]) == -15


# ============================================================================
# Test: split_arrow_map
# ============================================================================


def test_arrow_map_basic():
    """Test basic arrow parsing."""
    assert split_arrow_map("↔24→20→0840→V040") == ["24", "20", "0840", "V040"]


def test_arrow_map_single_state():
    """Test single state."""
    assert split_arrow_map("state") == ["state"]


def test_arrow_map_empty():
    """Test empty or whitespace."""
    assert split_arrow_map("") == []
    assert split_arrow_map("  ") == []


def test_arrow_map_with_spaces():
    """Test states with surrounding spaces."""
    assert split_arrow_map("A → B → C") == ["A", "B", "C"]


# ============================================================================
# Test: parse_number_row
# ============================================================================


def test_parse_number_row_basic():
    """Test basic number extraction."""
    assert parse_number_row("13 13 13 25") == [13.0, 13.0, 13.0, 25.0]


def test_parse_number_row_decimals():
    """Test decimal numbers."""
    assert parse_number_row("209 12.6 6") == [209.0, 12.6, 6.0]


def test_parse_number_row_negatives():
    """Test negative numbers."""
    assert parse_number_row("-5 3.14 -2.5") == [-5.0, 3.14, -2.5]


def test_parse_number_row_no_numbers():
    """Test string with no numbers."""
    assert parse_number_row("no numbers here") == []


def test_parse_number_row_empty():
    """Test empty string."""
    assert parse_number_row("") == []


# ============================================================================
# Test: pad_rows
# ============================================================================


def test_pad_rows_jagged():
    """Test padding jagged matrix."""
    result = pad_rows([[1, 2], [3, 4, 5]])
    assert result == [[1.0, 2.0, 0.0], [3.0, 4.0, 5.0]]


def test_pad_rows_already_rectangular():
    """Test already rectangular matrix."""
    result = pad_rows([[1, 2], [3, 4]])
    assert result == [[1.0, 2.0], [3.0, 4.0]]


def test_pad_rows_empty():
    """Test empty input."""
    assert pad_rows([]) == []


def test_pad_rows_custom_fill():
    """Test custom fill value."""
    result = pad_rows([[1, 2], [3, 4, 5]], fill=-1.0)
    assert result == [[1.0, 2.0, -1.0], [3.0, 4.0, 5.0]]


# ============================================================================
# Test: row_norm
# ============================================================================


def test_row_norm_basic():
    """Test Euclidean norm."""
    # sqrt(3^2 + 4^2) = sqrt(25) = 5
    assert row_norm([3, 4]) == 5.0


def test_row_norm_zero():
    """Test zero vector."""
    assert row_norm([0, 0, 0]) == 0.0


def test_row_norm_unit():
    """Test unit vector length."""
    assert row_norm([1, 1, 1]) == pytest.approx(1.7320508075688772)


def test_row_norm_empty():
    """Test empty row."""
    assert row_norm([]) == 0.0


# ============================================================================
# Test: matrix_from_rows & matrix_signature
# ============================================================================


def test_matrix_from_rows_basic():
    """Test matrix construction."""
    rows = ["13 13 13 25", "209 12.6 6"]
    matrix = matrix_from_rows(rows)
    assert len(matrix) == 2
    assert len(matrix[0]) == 4
    assert matrix[0][0] == 13.0


def test_matrix_signature_basic():
    """Test matrix signature computation."""
    sig = matrix_signature([[1, 2], [3, 4]])
    assert sig["rows"] == 2
    assert sig["cols"] == 2
    assert round(sig["sum"], 1) == 10.0
    assert round(sig["abs_sum"], 1) == 10.0
    assert len(sig["row_norms"]) == 2


def test_matrix_signature_empty():
    """Test empty matrix."""
    sig = matrix_signature([])
    assert sig["rows"] == 0
    assert sig["cols"] == 0
    assert sig["sum"] == 0.0
    assert sig["abs_sum"] == 0.0
    assert sig["row_norms"] == []


def test_matrix_signature_negative():
    """Test matrix with negative values."""
    sig = matrix_signature([[-1, -2], [3, 4]])
    assert sig["sum"] == 4.0
    assert sig["abs_sum"] == 10.0


# ============================================================================
# Test: neutral_zone_condition
# ============================================================================


def test_neutral_zone_stable():
    """Test stable condition."""
    result = neutral_zone_condition(
        force_net=[0.5, -0.3, 0.2],
        torque_net=0.1,
        force_tolerance=1.0,
        torque_tolerance=0.5,
    )
    assert result.stable is True
    assert result.force_within_tolerance is True
    assert result.torque_within_tolerance is True
    assert 0 < result.score <= 1


def test_neutral_zone_unstable_force():
    """Test unstable force."""
    result = neutral_zone_condition(
        force_net=[2.0, 0, 0],
        torque_net=0.1,
        force_tolerance=1.0,
        torque_tolerance=0.5,
    )
    assert result.stable is False
    assert result.force_within_tolerance is False


def test_neutral_zone_unstable_torque():
    """Test unstable torque."""
    result = neutral_zone_condition(
        force_net=0.1,
        torque_net=[1.0, 0, 0],
        force_tolerance=1.0,
        torque_tolerance=0.5,
    )
    assert result.stable is False
    assert result.torque_within_tolerance is False


# ============================================================================
# Test: neutral_stability_score
# ============================================================================


def test_neutral_stability_score_balanced():
    """Test balanced system."""
    score = neutral_stability_score(0.1, 0.05, 1.0, 0.5)
    assert 0 < score <= 1


def test_neutral_stability_score_zero():
    """Test zero force and torque."""
    score = neutral_stability_score(0.0, 0.0, 1.0, 1.0)
    assert score == 1.0  # exp(0) = 1


def test_neutral_stability_score_invalid_tolerance():
    """Test invalid tolerances."""
    with pytest.raises(ValueError):
        neutral_stability_score(0.1, 0.05, 0, 1.0)
    with pytest.raises(ValueError):
        neutral_stability_score(0.1, 0.05, 1.0, -0.5)


# ============================================================================
# Test: rotational_advantage
# ============================================================================


def test_rotational_advantage_basic():
    """Test rotational advantage calculation."""
    sn = 0.9
    ra = rotational_advantage([10, 0], [2, 0], sn)
    assert ra > 0


def test_rotational_advantage_zero_torque():
    """Test with minimal torque (uses epsilon)."""
    sn = 0.9
    ra = rotational_advantage([10, 0], [0, 0], sn, epsilon=1e-9)
    assert ra > 0


def test_rotational_advantage_invalid_epsilon():
    """Test invalid epsilon."""
    with pytest.raises(ValueError):
        rotational_advantage([10], [2], 0.9, epsilon=0)
    with pytest.raises(ValueError):
        rotational_advantage([10], [2], 0.9, epsilon=-0.1)


def test_rotational_advantage_invalid_score():
    """Test invalid neutral score."""
    with pytest.raises(ValueError):
        rotational_advantage([10], [2], -0.1)
