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

    for index in range(0, len(data), 3):
        column1: List[int] = []
        column2: List[int] = []
        column3: List[int] = []
        for step in range(3):
            line = data[index + step]
            numbers: List[str] = re.split(r"\s+", line.strip())
            n1, n2, n3 = int(numbers[0]), int(numbers[1]), int(numbers[2])

            column1.append(n1)
            column2.append(n2)
            column3.append(n3)

        triangles.append(Triangle(column1[0], column1[1], column1[2]))
        triangles.append(Triangle(column2[0], column2[1], column2[2]))
        triangles.append(Triangle(column3[0], column3[1], column3[2]))

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
    print(solution("./input.txt"))  # 1921
