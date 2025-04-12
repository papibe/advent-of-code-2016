import re
from typing import List, Match, Optional


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()
    return data


def solve(sequence: str) -> int:
    output: List[str] = []
    index: int = 0

    marker_regex: str = r"^\((\d+)x(\d+)\)"

    while len(sequence) > 0:
        matches: Optional[Match[str]] = re.match(marker_regex, sequence)

        if matches:
            amount: int = int(matches.group(1))
            times: int = int(matches.group(2))

            index = len(matches.group(0))

            for _ in range(times):
                for i in range(index, index + amount):
                    output.append(sequence[i])

            index += amount

        else:
            output.append(sequence[0])
            index = 1

        sequence = sequence[index:]

        # print(f"{sequence = }")
        # print(output)
    return len(output)


def solution(filename: str) -> int:
    sequence: str = parse(filename)
    return solve(sequence)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 110346
