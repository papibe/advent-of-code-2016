import pytest

from part1 import solution


@pytest.mark.parametrize(
    "string,expected",
    [
        ("ihgpwlah", "DDRRRD"),
        ("kglvqrro", "DDUDRLRRUDRD"),
        ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
    ],
    ids=[
        "ihgpwlah_should_be_DDRRRD",
        "kglvqrro_should_be_DDUDRLRRUDRD",
        "ulqzkmiv_should_be_DRURDRUDDLLDLUURRDULRLDUUDDDRR",
    ],
)
def test_solution(string: str, expected: str) -> None:
    result: str = solution(string)
    assert result == expected, f"got {result}, needs {expected}"
