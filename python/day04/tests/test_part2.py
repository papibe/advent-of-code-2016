import pytest

from part2 import Room


@pytest.mark.parametrize(
    "name,sector,expected",
    [
        ("qzmt-zixmtkozy-ivhz", "343", "very encrypted name"),
    ],
)
def test_part1(name: str, sector: int, expected: int) -> None:
    room: Room = Room("", name, int(sector), "")
    result: str = room.decrypt()
    assert result == expected, f"got {result}, needs {expected}"
