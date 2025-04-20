import pytest

from part2 import uncompress


@pytest.mark.parametrize(
    "sequence,expected",
    [
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
    ids=[
        "(3x3)XYZ should be  9",
        "X(8x2)(3x3)ABCY should be  20",
        "(27x12)(20x12)(13x14)(7x10)(1x12)A should be  241920",
        "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN should be  445",
    ],
)
def test_part1(sequence: str, expected: int) -> None:
    result: int = uncompress(sequence)
    assert result == expected, f"got {result}, needs {expected}"
