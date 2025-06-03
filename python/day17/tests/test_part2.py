import pytest

from part2 import solution


@pytest.mark.parametrize(
    "string,expected",
    [
        ("ihgpwlah", 370),
        ("kglvqrro", 492),
        ("ulqzkmiv", 830),
    ],
    ids=[
        "ihgpwlah_should_be_370",
        "kglvqrro_should_be_492",
        "ulqzkmiv_should_be_830",
    ],
)
def test_solution(string: str, expected: int) -> None:
    result: int = solution(string)
    assert result == expected, f"got {result}, needs {expected}"
