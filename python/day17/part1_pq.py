import heapq as hq
from typing import Dict, List, Tuple

from md5_hash import md5_short_hash

State = Tuple[int, int, int, List[str]]

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

WALL: str = "#"
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
    # BFS init
    heap: List[State] = [(0, 1, 1, [])]
    hq.heapify(heap)

    # BFS
    while heap:
        steps, row, col, path = hq.heappop(heap)

        if MAZE[row][col] == VAULT:
            return "".join(path)

        # SPACE or START
        hashed: str = md5_short_hash(passcode + "".join(path))
        for d, code in zip(DOORS, hashed):

            if code in OPEN_DOOR_CODE:
                row_step, col_step = STEPS[d]
                neighbor_row: int = row + row_step
                neighbor_col: int = col + col_step

                if MAZE[neighbor_row][neighbor_col] != WALL:
                    new_path = path.copy()
                    new_path.append(d)
                    hq.heappush(
                        heap,
                        (steps + 1, row + 2 * row_step, col + 2 * col_step, new_path),
                    )

    return ""


if __name__ == "__main__":
    print(solution("yjjvjgan"))  # RLDRUDRDDR
