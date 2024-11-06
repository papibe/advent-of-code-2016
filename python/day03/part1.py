import re
from dataclasses import dataclass
from typing import List


@dataclass
class Triangle:
    side1: int
    side2: int
    side3: int

    def _check(self, s1: int, s2: int, s3: int) -> bool:
        return s1 + s2 > s3

    def check(self) -> bool:
        return (
            self._check(self.side1, self.side2, self.side3)
            and self._check(self.side1, self.side3, self.side2)
            and self._check(self.side2, self.side3, self.side1)
        )


def parse(filename: str) -> List[Triangle]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    triangles: List[Triangle] = []

    for line in data:
        sides: List[str] = re.split(r"\s+", line.strip())
        side1, side2, side3 = int(sides[0]), int(sides[1]), int(sides[2])

        triangles.append(Triangle(side1, side2, side3))

    return triangles


def solve(triangles: List[Triangle]) -> int:
    possibles: int = 0

    for triangle in triangles:
        if triangle.check():
            possibles += 1

    return possibles


def solution(filename: str) -> int:
    triangles: List[Triangle] = parse(filename)
    return solve(triangles)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 1050
