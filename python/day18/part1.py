import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

SAFE: str = "."
TRAP: str = "^"

def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip()

    return data


def solve(tiles: List[str], times: int) -> int:
    n: int = len(tiles)
    safe_tiles: int = len([tile for tile in tiles if tile == SAFE])

    for _ in range(times - 1):
        next_tiles: List[str] = [SAFE] * n

        for index in range(n):
            next_tile: str = SAFE

            left: str = tiles[index - 1] if index >= 1 else SAFE
            center: str = tiles[index]
            right: str = tiles[index + 1] if index < n - 1 else SAFE

            rule1: bool = (left == TRAP and center == TRAP and right == SAFE)
            rule2: bool = (center == TRAP and right == TRAP and left == SAFE)
            rule3: bool = (left == TRAP and center == SAFE and right == SAFE)
            rule4: bool = (right == TRAP and left == SAFE and center == SAFE)

            if rule1 or rule2 or rule3 or rule4:
                next_tile = TRAP

            next_tiles[index] = next_tile

        tiles = next_tiles
        safe_tiles += len([tile for tile in tiles if tile == SAFE])

    return safe_tiles


def solution(filename: str, times: int) -> int:
    tiles: List[str] = parse(filename)
    return solve(tiles, times)


if __name__ == "__main__":
    print(solution("./input.txt", 40))  # 2013
