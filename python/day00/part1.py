import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    for line in data:
        pass

    return data


def solve(data: List[str]) -> int:
    total_sum: int = 0

    for row in data:
        pass

    return total_sum


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
