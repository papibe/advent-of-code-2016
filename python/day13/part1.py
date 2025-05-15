from collections import deque
from typing import Deque, Set, Tuple


def is_open(x: int, y: int, favorite_number: int) -> bool:
    value: int = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    bin_str: str = f"{value:b}"
    ones: int = sum([int(digit) for digit in bin_str])
    return ones % 2 == 0


def solution(favorite_number: int, xgoal: int, ygoal: int) -> int:
    # BFS setup
    queue: Deque[Tuple[int, int, int]] = deque([(1, 1, 0)])
    visited: Set[Tuple[int, int]] = set([(1, 1)])

    # BFS
    while queue:
        x, y, steps = queue.popleft()
        if x == xgoal and y == ygoal:
            return steps

        for newx, newy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (
                newx >= 0
                and newy >= 0
                and is_open(newx, newy, favorite_number)
                and (newx, newy) not in visited
            ):
                queue.append((newx, newy, steps + 1))
                visited.add((newx, newy))

    return -1


if __name__ == "__main__":
    print(solution(10, 7, 4))  # 11
    print(solution(1362, 31, 39))  # 82
