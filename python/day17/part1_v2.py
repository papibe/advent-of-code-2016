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


def solution(passcode: str) -> str:

    shortest_len: int = float("inf")  # type: ignore
    shortest_path: List[str] = []

    def dfs(row: int, col: int, path: List[str]) -> None:
        nonlocal shortest_len
        nonlocal shortest_path

        if MAZE[row][col] == VAULT:
            if len(path) < shortest_len:
                shortest_len = len(path)
                shortest_path = path.copy()
            return

        if len(path) + 1 >= shortest_len:
            return

        # SPACE or START
        hashed: str = md5_short_hash(passcode + "".join(path))
        for d, code in zip(DOORS, hashed):

            if code in OPEN_DOOR_CODE:
                row_step, col_step = STEPS[d]
                neighbor_row: int = row + row_step
                neighbor_col: int = col + col_step

                if MAZE[neighbor_row][neighbor_col] != WALL:
                    path.append(d)
                    dfs(row + 2 * row_step, col + 2 * col_step, path)
                    path.pop()
        return

    dfs(row=1, col=1, path=[])
    return "".join(shortest_path)


if __name__ == "__main__":
    print(solution("yjjvjgan"))  # RLDRUDRDDR
