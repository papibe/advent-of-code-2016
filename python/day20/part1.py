from dataclasses import dataclass
from typing import List


@dataclass
class Range:
    low: int
    high: int


def parse(filename: str) -> List[Range]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    ranges: List[Range] = []

    for line in data:
        splitted_line: List[str] = line.split("-")
        ranges.append(
            Range(
                int(splitted_line[0]),
                int(splitted_line[1]),
            )
        )

    return ranges


def solve(ranges: List[Range]) -> int:
    min_ip: int = 0

    sorted_ranges: List[Range] = sorted(ranges, key=lambda x: (x.low, x.high))

    for r in sorted_ranges:
        if r.low <= min_ip <= r.high:
            min_ip = r.high + 1

    return min_ip


def solution(filename: str) -> int:
    ranges: List[Range] = parse(filename)
    return solve(ranges)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3
    print(solution("./input.txt"))  # 23923783
