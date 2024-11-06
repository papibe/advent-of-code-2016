from dataclasses import dataclass
from typing import List


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

    def move(self, instruction: Instruction) -> None:
        # rotate
        prev_row: int = self.row_dir
        prev_col: int = self.col_dir
        if instruction.direction == "R":
            self.row_dir = prev_col
            self.col_dir = -prev_row
        else:
            self.row_dir = -prev_col
            self.col_dir = prev_row

        # move forward
        self.row += instruction.steps * self.row_dir
        self.col += instruction.steps * self.col_dir

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

    for instruction in instructions:
        location.move(instruction)

    return location.get_distance()


def solution(filename: str) -> int:
    instructions: List[Instruction] = parse(filename)
    location: Location = Location()
    return solve(instructions, location)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 250
