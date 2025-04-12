import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


def joseph_180(n: int) -> int:
    print(n)
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 3

    mod = n % 3
    if mod == 0:
        l = n // 3
    else:
        l = (n + 2) // 3

    if mod == 0:
        return 3 * joseph_180(l)

    half = l // 2
    v = joseph_180(l)

    if v <= half:
        return (3 * v) - (3 - mod)
    else:
        return (3 * v) - 2* (3 - mod)


def solution(number_of_elves: int) -> int:
    return joseph_180(number_of_elves)


if __name__ == "__main__":
    # print(solution(5))  # 2
    print(solution(3014387))  # 1420064
