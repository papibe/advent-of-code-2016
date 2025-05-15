from typing import List

from part1 import is_open

WALL: str = "#"
SPACE: str = "."

layout: List[str] = [
    ".#.####.##",
    "..#..#...#",
    "#....##...",
    "###.#.###.",
    ".##..#..#.",
    "..##....#.",
    "#...##.###",
]


def test_is_open() -> None:
    for y, row in enumerate(layout):
        for x, cube in enumerate(row):
            if is_open(x, y, 10):
                assert cube == SPACE
            else:
                assert cube == WALL
