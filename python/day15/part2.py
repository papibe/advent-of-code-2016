import re
from dataclasses import dataclass
from typing import List, Match, Optional


@dataclass
class Disc:
    id_: int
    slots: int
    time: int
    initial_pos: int


def parse(filename: str) -> List[Disc]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    disc_regex: str = (
        r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)"
    )
    discs: List[Disc] = []

    for line in data:
        matches: Optional[Match[str]] = re.match(disc_regex, line)
        assert matches is not None

        disc_id: int = int(matches.group(1))
        slots: int = int(matches.group(2))
        time: int = int(matches.group(3))
        initial_position: int = int(matches.group(4))

        discs.append(Disc(disc_id, slots, time, initial_position))

    return discs


def solve(discs: List[Disc]) -> int:
    timestamp: int = 0
    while True:
        for time_shift, disc in enumerate(discs, 1):
            position: int = (disc.initial_pos + timestamp + time_shift) % disc.slots
            if position != 0:
                break
        else:
            return timestamp
        timestamp += 1


def solution(filename: str) -> int:
    discs: List[Disc] = parse(filename)
    # patch for part 2
    discs.append(Disc(id_=100, slots=11, time=0, initial_pos=0))
    return solve(discs)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 2408135
