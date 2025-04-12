import pytest

from part1 import solve


@pytest.mark.parametrize(
    "tiles,rows,expected",
    [
        ("..^^.", 3, 6),
        (".^^.^.^^^^", 10, 38),
    ],
    ids=[
        "..^^._should_be_6",
        ".^^.^.^^^^_should_be_38",
    ],
)
def test_part1(tiles: str, rows: int, expected: int) -> None:
    result: int = solve(tiles, rows)
    assert result == expected, f"got {result}, needs {expected}"
