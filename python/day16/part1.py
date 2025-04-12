import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def check_sum(data: List[str]) -> str:

    checksum: List[str] = []

    while True:
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

        # print("".join(checksum))

    return "".join(checksum)



def solution(puzzle_input: str, length: int) -> int:

    a: List[str] = list(puzzle_input)

    while len(a) < length:
        a_reversed: List[str] = reversed(a)
        a.append("0")
        for char in a_reversed:
            if char == "1":
                a.append("0")
            else:
                a.append("1")

    return check_sum(a[:length])


if __name__ == "__main__":
    print(solution("10000", 20))  # 01100
    print(solution("10001110011110000", 272))  # 10010101010011101
