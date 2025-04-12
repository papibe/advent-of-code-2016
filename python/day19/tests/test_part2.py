import pytest

from part2 import joseph_180


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (3, 3),
        (4, 1),
        (5, 2),
    ],
    ids=[
        "1_should_be_1",
        "2_should_be_1",
        "3_should_be_3",
        "4_should_be_1",
        "5_should_be_2",
    ],
)
def test_josephus(n: int, expected: int) -> None:
    result: int = joseph_180(n)
    assert result == expected, f"got {result}, needs {expected}"
