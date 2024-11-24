import re
from dataclasses import dataclass
from enum import Enum
from typing import List, Match, Optional, Tuple


class InstructionType(Enum):
    RECT: str = "r"
    ROT_ROW: str = "rr"
    ROT_COL: str = "rc"


@dataclass
class Instruction:
    type_: InstructionType
    a: int
    b: int


class Display:
    def __init__(self, rows: int, cols: int):
        self.grid: List[List[str]] = [["."] * cols for _ in range(rows)]
        self.rows: int = rows
        self.cols: int = cols

    def rect(self, a: int, b: int) -> None:
        cols: int = a
        rows: int = b

        for row in range(rows):
            for col in range(cols):
                self.grid[row][col] = "#"

    def rot_row(self, a: int, b: int) -> None:
        row: int = a
        shift: int = b

        original_row: List[str] = self.grid[row].copy()

        for col in range(self.cols):
            self.grid[row][(col + shift) % self.cols] = original_row[col]

    def rot_col(self, a: int, b: int) -> None:
        col: int = a
        shift: int = b

        original_col: List[str] = [""] * self.rows
        for row in range(self.rows):
            original_col[row] = self.grid[row][col]

        for row in range(self.rows):
            self.grid[(row + shift) % self.rows][col] = original_col[row]

    def count(self) -> int:
        counter: int = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "#":
                    counter += 1

        return counter

    def print(self) -> None:
        output: List[str] = []
        for row in range(self.rows):
            for col in range(self.cols):
                output.append(self.grid[row][col])
            output.append("\n")
        return "".join(output)


def parse(filename: str) -> List[Instruction]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rect_regex: str = r"rect (\d+)x(\d+)"
    rotrow_regex: str = r"rotate row y=(\d+) by (\d+)"
    rotrcol_regex: str = r"rotate column x=(\d+) by (\d+)"

    instructions: List[Instruction] = []

    for line in data:
        rect_match: Optional[Match[str]] = re.match(rect_regex, line)
        rotrow_match: Optional[Match[str]] = re.match(rotrow_regex, line)
        rotcol_match: Optional[Match[str]] = re.match(rotrcol_regex, line)

        instruction_type: InstructionType
        a: int
        b: int

        if rect_match:
            a = int(rect_match.group(1))
            b = int(rect_match.group(2))
            instruction_type = InstructionType.RECT

        elif rotrow_match:
            a = int(rotrow_match.group(1))
            b = int(rotrow_match.group(2))
            instruction_type = InstructionType.ROT_ROW

        elif rotcol_match:
            a = int(rotcol_match.group(1))
            b = int(rotcol_match.group(2))
            instruction_type = InstructionType.ROT_COL

        else:
            raise Exception("Unable to match instruction")

        instructions.append(Instruction(instruction_type, a, b))

    return instructions


def solve(instructions: List[Instruction], display: Display) -> Tuple[int, str]:
    for instruction in instructions:
        # print(instruction)
        match instruction.type_:
            case InstructionType.RECT:
                display.rect(instruction.a, instruction.b)

            case InstructionType.ROT_ROW:
                display.rot_row(instruction.a, instruction.b)

            case InstructionType.ROT_COL:
                display.rot_col(instruction.a, instruction.b)

            case _:
                pass

    return display.count(), display.print()


def solution(filename: str, rows: int, cols: int) -> int:
    instructions: List[Instruction] = parse(filename)
    display: Display = Display(rows, cols)

    return solve(instructions, display)


if __name__ == "__main__":
    lit_example, example_display = solution("./example.txt", 3, 7)  # 6
    lit_pixels, display = solution("./input.txt", 6, 50)  # 115 and EFEYKFRFIJ

    print("Example")
    print("-------")
    print("display:")
    print(example_display, end="")
    print(f"lit pixels: {lit_example}")
    print()
    print("Both parts")
    print("----------")
    print("display (part 2):")
    print(display, end="")
    print(f"lit pixels (part 1): {lit_pixels}")
