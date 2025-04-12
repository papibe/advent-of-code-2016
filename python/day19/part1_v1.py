import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

NO_PRESENTS: int = 0

def solution(n: int) -> int:
    elves: List[int] = list(range(1, n + 1))

    while len(elves) >= 2:
        new_elves: List[int] = []
        for index in range(0, len(elves), 2):
            skipped_elf_index: int = (index + 1) % len(elves)
            elves[skipped_elf_index] = NO_PRESENTS

        for elf in elves:
            if elf != NO_PRESENTS:
                new_elves.append(elf)

        # print(new_elves)

        elves = new_elves


    return elves[0]


if __name__ == "__main__":
    print(solution(5))  # 3
    print(solution(3014387))  # 1834471
