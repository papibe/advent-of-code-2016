from typing import List

import pytest

from part1 import solve


@pytest.mark.parametrize(
    "str_tiles,rows,expected",
    [
        ("..^^.", 3, 6),
        (".^^.^.^^^^", 10, 38),
    ],
    ids=[
        "..^^._should_be_6",
        ".^^.^.^^^^_should_be_38",
    ],
)
def test_part1(str_tiles: str, rows: int, expected: int) -> None:
    tiles: List[str] = [char for char in str_tiles]
    result: int = solve(tiles, rows)
    assert result == expected, f"got {result}, needs {expected}"
