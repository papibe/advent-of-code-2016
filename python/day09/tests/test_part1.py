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
    ids=[
        "ADVENT_should_be_6",
        "A(1x5)BC_should_be_7",
        "(3x3)XYZ_should_be_9",
        "A(2x2)BCD(2x2)EFG_should_be_11",
        "(6x1)(1x3)A_should_be_6",
        "X(8x2)(3x3)ABCY_should_be_18",
    ],
)
def test_part1(sequence: str, expected: int) -> None:
    result: int = solve(sequence)
    assert result == expected, f"got {result}, needs {expected}"
