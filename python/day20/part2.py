from dataclasses import dataclass
from typing import List

LAST: int = -1


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


def solve(ranges: List[Range], max_ip: int) -> int:
    sorted_ranges: List[Range] = sorted(ranges, key=lambda x: (x.low, x.high))
    joined_ranges: List[Range] = [sorted_ranges[0]]

    for incoming in sorted_ranges[1:]:
        last: Range = joined_ranges.pop()
        if incoming.low <= last.high + 1:
            joined_ranges.append(Range(last.low, max(last.high, incoming.high)))
        else:
            joined_ranges.append(last)
            joined_ranges.append(incoming)

    allowed_ips: int = 0
    last_value: int = 0

    for range_ in joined_ranges:
        if range_.low > last_value:
            allowed_ips += range_.low - last_value - 1
        last_value = range_.high

    if last_value < max_ip:
        allowed_ips += max_ip - last_value

    return allowed_ips


def solution(filename: str, max_ip: int) -> int:
    ranges: List[Range] = parse(filename)
    return solve(ranges, max_ip)


if __name__ == "__main__":
    print(solution("./example.txt", 9))  # 2
    print(solution("./input.txt", 4294967295))  # 125
