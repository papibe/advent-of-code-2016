import pytest

from part1 import josephus


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (3, 3),
        (4, 1),
        (5, 3),
        (6, 5),
        (10, 5),
        (40, 17),
    ],
    ids=[
        "1_should_be_1",
        "2_should_be_1",
        "3_should_be_3",
        "4_should_be_1",
        "5_should_be_3",
        "6_should_be_5",
        "10_should_be_5",
        "40_should_be_17",
    ],
)
def test_josephus(n: int, expected: int) -> None:
    result: int = josephus(n)
    assert result == expected, f"got {result}, needs {expected}"
