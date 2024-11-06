import pytest

from part1 import solve


@pytest.mark.parametrize(
    "sequence,expected",
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ],
    # ids=[
    #     "aa_bb_cc_dd_ee_should_be_True",
    #     "aa_bb_cc_dd_aa_should_be_False",
    #     "aa_bb_cc_dd_aaa_should_be_True",
    # ],
)
def test_part1(sequence: str, expected: int) -> None:
    result: int = solve(sequence)
    assert result == expected, f"got {result}, needs {expected}"
