from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Instruction:
    direction: str
    steps: int


class Location:
    def __init__(self) -> None:
        self.row: int = 0
        self.col: int = 0
        self.row_dir: int = -1
        self.col_dir: int = 0

    def turn(self, direction: str) -> None:
        # rotate
        prev_row: int = self.row_dir
        prev_col: int = self.col_dir

        if direction == "R":
            self.row_dir = prev_col
            self.col_dir = -prev_row
        else:
            self.row_dir = -prev_col
            self.col_dir = prev_row

    def move(self, distance: int) -> Tuple[int, int]:
        # move forward
        self.row += distance * self.row_dir
        self.col += distance * self.col_dir

        return (self.row, self.col)

    def get_distance(self) -> int:
        return abs(self.row) + abs(self.col)


def parse(filename: str) -> List[Instruction]:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

    instructions: List[Instruction] = []

    for instruction in data.split(", "):
        direction: str = instruction[0]
        steps: int = int(instruction[1:])
        instructions.append(Instruction(direction, steps))

    return instructions


def solve(instructions: List[Instruction], location: Location) -> int:

    visited: Set[Tuple[int, int]] = set([(0, 0)])

    for instruction in instructions:
        location.turn(instruction.direction)

        for _ in range(instruction.steps):
            position: Tuple[int, int] = location.move(1)

            if position in visited:
                return location.get_distance()

            visited.add(position)

    return -1


def solution(filename: str) -> int:
    instructions: List[Instruction] = parse(filename)
    location: Location = Location()
    return solve(instructions, location)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 151
