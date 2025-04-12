import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple, Iterable


def check_sum(data: List[str]) -> str:

    checksum: List[str] = []

    counter: int = 0
    while True:
        counter += 1
        checksum: List[str] = []
        for index in range(0, len(data), 2):
            if data[index] == data[index + 1]:
                checksum.append("1")
            else:
                checksum.append("0")

        if len(checksum) % 2 != 0:
            break
        else:
            data = checksum

    return "".join(checksum)



def solve(puzzle_input: str, length: int) -> int:

    a: List[str] = list(puzzle_input)

    counter: int = 0
    while len(a) < length:
        a_reversed: Iterable[str] = reversed(a)
        a.append("0")
        counter += 1
        for char in a_reversed:
            if char == "1":
                a.append("0")
            else:
                a.append("1")

    return a[:length]

def solution(puzzle_input: str, length: int) -> int:
    data = solve(puzzle_input, length)
    return check_sum(data)

if __name__ == "__main__":
    print(solution("10001110011110000", 35651584))  # 01100111101101111
