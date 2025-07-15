import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, List, Match, Optional, Set, Tuple

INVALID: int = -1

MainQueueItem = Tuple[int, Tuple[int, int], Tuple[int, int]]
SecondaryQueueItem = Tuple[int, Tuple[int, int]]
VisitedItem = Tuple[Tuple[int, int], Tuple[int, int]]
GridMatrix = List[List["Node"]]


@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    avail: int


class Grid:
    def __init__(
        self, grid: GridMatrix, empty_y: int, empty_x: int, g_y: int, g_x: int
    ) -> None:
        self.grid: GridMatrix = grid
        self.Y = len(self.grid)
        self.X = len(self.grid[0])
        self.empty_y: int = empty_y
        self.empty_x: int = empty_x
        self.g_y: int = g_y
        self.g_x: int = g_x
        self.max_size: int = self.grid[self.empty_y][self.empty_x].size


def get_neighbors(y: int, x: int, size_y: int, size_x: int) -> List[Tuple[int, int]]:
    neighbors: List[Tuple[int, int]] = []

    for new_y, new_x in [
        (y - 1, x),
        (y, x - 1),
        (y + 1, x),
        (y, x + 1),
    ]:
        if 0 <= new_y < size_y and 0 <= new_x < size_x:
            neighbors.append((new_y, new_x))

    return neighbors


def get_empty(grid: List[List[Node]]) -> Tuple[int, int]:
    for y, line in enumerate(grid):
        for x, node in enumerate(line):
            if node.used == 0:
                return y, x
    return -1, -1


def parse(filename: str) -> Grid:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    re_node: str = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"

    nodes: List[Node] = []
    max_x: int = -1
    max_y: int = -1

    for i in range(2, len(data)):
        line: str = data[i]
        matches: Optional[Match[str]] = re.match(re_node, line)

        assert matches is not None

        x: int = int(matches.group(1))
        y: int = int(matches.group(2))
        size: int = int(matches.group(3))
        used: int = int(matches.group(4))
        avail: int = int(matches.group(5))
        _percentage_used: int = int(matches.group(6))

        nodes.append(Node(x, y, size, used, avail))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        if used == 0:
            empty_y: int = y
            empty_x: int = x

    dummy_node: Node = Node(0, 0, 0, 0, 0)

    grid: GridMatrix = [[dummy_node] * (max_x + 1) for _ in range((max_y + 1))]
    for node in nodes:
        grid[node.y][node.x] = node

    assert max_x == len(grid[0]) - 1

    return Grid(grid, empty_y, empty_x, 0, max_x)


def move_empty_to_neighbor(
    grid: Grid,
    current_y: int,
    current_x: int,
    destination_y: int,
    destination_x: int,
    g_y: int,
    g_x: int,
) -> int:

    # BFS init
    steps: int = 0
    queue: Deque[SecondaryQueueItem] = deque([(0, (current_y, current_x))])
    visited: Set[Tuple[int, int]] = set([(current_y, current_x)])

    # BFS
    while queue:
        steps, (current_y, current_x) = queue.popleft()

        if (current_y, current_x) == (destination_y, destination_x):
            return steps

        for neighbor_y, neighbor_x in get_neighbors(
            current_y, current_x, grid.Y, grid.X
        ):

            # skip full nodes (#)
            if grid.grid[neighbor_y][neighbor_x].used > grid.max_size:
                continue

            # don't pass over G
            if (neighbor_y, neighbor_x) == (g_y, g_x):
                continue

            if (neighbor_y, neighbor_x) in visited:
                continue

            queue.append((steps + 1, (neighbor_y, neighbor_x)))
            visited.add((neighbor_y, neighbor_x))

    return INVALID


def solve(
    grid: Grid,
    current_y: int,
    current_x: int,
    empty_y: int,
    empty_x: int,
    destination_y: int,
    destination_x: int,
) -> int:

    # BFS init
    queue: Deque[MainQueueItem] = deque(
        [(0, (current_y, current_x), (empty_y, empty_x))]
    )
    visited: Set[VisitedItem] = set([((current_y, current_x), (empty_y, empty_x))])

    # BFS
    while queue:
        steps, (current_y, current_x), (empty_y, empty_x) = queue.popleft()

        if (current_y, current_x) == (destination_y, destination_x):
            return steps

        for neighbor_y, neighbor_x in get_neighbors(
            current_y, current_x, grid.Y, grid.X
        ):
            # skip full nodes (#)
            if grid.grid[neighbor_y][neighbor_x].used > grid.max_size:
                continue

            if ((neighbor_y, neighbor_x), (current_y, current_x)) in visited:
                continue

            # move empty space to neighbor
            intermediate_steps = move_empty_to_neighbor(
                grid,
                empty_y,
                empty_x,
                neighbor_y,
                neighbor_x,
                current_y,
                current_x,
            )

            assert intermediate_steps != INVALID

            queue.append(
                (
                    steps + intermediate_steps + 1,
                    (neighbor_y, neighbor_x),
                    (current_y, current_x),
                )
            )
            visited.add(((neighbor_y, neighbor_x), (current_y, current_x)))

    return INVALID


def solution(filename: str) -> int:
    grid = parse(filename)

    return solve(
        grid=grid,
        current_y=grid.g_y,
        current_x=grid.g_x,
        empty_y=grid.empty_y,
        empty_x=grid.empty_x,
        destination_y=0,
        destination_x=0,
    )


if __name__ == "__main__":
    print(solution("./example.txt"))  # 7
    print(solution("./input.txt"))  # 215
