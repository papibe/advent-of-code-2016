from typing import List, Tuple

KeypadRow = Tuple[str, str, str, str, str, str, str]
Keypad = Tuple[
    KeypadRow, KeypadRow, KeypadRow, KeypadRow, KeypadRow, KeypadRow, KeypadRow
]

KEYPAD: Keypad = (
    (".", ".", ".", ".", ".", ".", "."),
    (".", ".", ".", "1", ".", ".", "."),
    (".", ".", "2", "3", "4", ".", "."),
    (".", "5", "6", "7", "8", "9", "."),
    (".", ".", "A", "B", "C", ".", "."),
    (".", ".", ".", "D", ".", ".", "."),
    (".", ".", ".", ".", ".", ".", "."),
)


class DIR:
    UP: str = "U"
    DOWN: str = "D"
    LEFT: str = "L"
    RIGHT: str = "R"


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()
    return data


def solve(instructions: List[str]) -> str:
    codes: List[str] = []

    current_row: int = 3
    current_col: int = 1

    new_row: int
    new_col: int

    for row in instructions:
        for direction in row:
            match direction:
                case DIR.UP:
                    new_row = current_row - 1
                    if KEYPAD[new_row][current_col] != ".":
                        current_row = new_row

                case DIR.DOWN:
                    new_row = current_row + 1
                    if KEYPAD[new_row][current_col] != ".":
                        current_row = new_row

                case DIR.LEFT:
                    new_col = current_col - 1
                    if KEYPAD[current_row][new_col] != ".":
                        current_col = new_col

                case DIR.RIGHT:
                    new_col = current_col + 1
                    if KEYPAD[current_row][new_col] != ".":
                        current_col = new_col

        codes.append(KEYPAD[current_row][current_col])

    return "".join(codes)


def solution(filename: str) -> str:
    instructions: List[str] = parse(filename)
    return solve(instructions)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 5DB3
    print(solution("./input.txt"))  # AC8C8
