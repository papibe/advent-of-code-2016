from typing import Dict, List, Tuple

from md5_hash import md5_short_hash

MAZE: List[str] = [
    "#########",
    "#S| | | #",
    "#-#-#-#-#",
    "# | | | #",
    "#-#-#-#-#",
    "# | | | #",
    "#-#-#-#-#",
    "# | | |V#",
    "#########",
]

START: str = "S"
WALL: str = "#"
SPACE: str = " "
VAULT: str = "V"

DOORS: List[str] = ["U", "D", "L", "R"]

STEPS: Dict[str, Tuple[int, int]] = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

OPEN_DOOR_CODE: str = "bcdef"


def solve(
    passcode: str, row: int, col: int, path: List[str], solutions: List[List[str]]
) -> None:

    if MAZE[row][col] == VAULT:
        return solutions.append(path.copy())

    # SPACE or START
    hashed: str = md5_short_hash(passcode + "".join(path))
    for d, code in zip(DOORS, hashed):

        if code in OPEN_DOOR_CODE:
            row_step, col_step = STEPS[d]
            neighbor_row: int = row + row_step
            neighbor_col: int = col + col_step

            if MAZE[neighbor_row][neighbor_col] != WALL:
                path.append(d)
                solve(passcode, row + 2 * row_step, col + 2 * col_step, path, solutions)
                path.pop()

    return


def solution(passcode: str) -> int:
    path: List[str] = []
    solutions: List[List[str]] = []

    solve(passcode=passcode, row=1, col=1, path=path, solutions=solutions)

    longest_len: int = float("-inf")  # type: ignore

    for p in solutions:
        if len(p) > longest_len:
            longest_len = len(p)

    return longest_len


if __name__ == "__main__":
    print(solution("yjjvjgan"))  # 830
