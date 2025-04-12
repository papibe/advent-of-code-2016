import pytest

from part1 import check_sum, solution


@pytest.mark.parametrize(
    "data,expected",
    [
        ("110010110100", "100"),
        ("10000011110010000111", "01100")
    ],
    ids=[
        "110010110100_should_be_100",
        "10000011110010000111_should_be_01100",
    ],
)
def test_check(data: str, expected: str) -> None:
    result: int = check_sum(data)
    assert result == expected, f"got {result}, needs {expected}"

def test_solution_for_10000_20_should_be_01100() -> None:
    expected: str = "01100"
    result: int = solution("10000", 20)
    assert result == expected, f"got {result}, needs {expected}"
