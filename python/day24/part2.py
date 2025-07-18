from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Set, Tuple

WALL: str = "#"


@dataclass
class Position:
    row: int
    col: int

    def __hash__(self) -> int:
        return self.row * 27 + self.col * 31


Node = int
AdjacencyMatrix = List[List[Node]]
Positions = Dict[Node, Position]
QueueItem = Tuple[int, Position]


def get_shortest_distance(
    grid: List[str],
    am: AdjacencyMatrix,
    node_positions: Positions,
    node: Node,
    other_node: Node,
) -> int:
    # BFS setup
    queue: Deque[QueueItem] = deque([(0, node_positions[node])])
    visited: Set[Position] = set([node_positions[node]])

    # print(f"{visited = }")

    # BFS
    while queue:
        steps, pos = queue.popleft()

        if pos == node_positions[other_node]:
            return steps

        for new_row, new_col in [
            (pos.row + 1, pos.col),
            (pos.row - 1, pos.col),
            (pos.row, pos.col + 1),
            (pos.row, pos.col - 1),
        ]:
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == WALL:
                    continue

                new_position: Position = Position(new_row, new_col)
                if new_position not in visited:
                    queue.append((steps + 1, new_position))
                    visited.add(new_position)

    return -1


def parse(filename: str) -> Tuple[AdjacencyMatrix, Positions]:
    with open(filename, "r") as fp:
        grid: List[str] = fp.read().splitlines()

    # first pass get nodes
    node_positions: Positions = {}
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell.isnumeric():
                node_positions[int(cell)] = Position(row, col)

    n: int = len(node_positions)
    # adjacency_matrix
    am: AdjacencyMatrix = [[float("inf")] * n for _ in range(n)]  # type: ignore

    # calculate mutual distances:
    for node in range(n):
        am[node][node] = 0

    for node in range(n):
        for other_node in range(node + 1, n):
            distance: int = get_shortest_distance(
                grid, am, node_positions, node, other_node
            )
            am[node][other_node] = distance
            am[other_node][node] = distance

    return am, node_positions


def solve(am: AdjacencyMatrix, start_node: Node, number_of_nodes: int) -> int:

    min_distance: int = float("inf")  # type: ignore
    visited: List[bool] = [False] * number_of_nodes

    def dfs(node: Node, steps: int) -> None:
        nonlocal min_distance

        if all(visited):
            min_distance = min(min_distance, steps + am[node][0])
            return

        visited[node] = True

        for other_node in range(number_of_nodes):
            if not visited[other_node]:
                visited[other_node] = True
                dfs(other_node, steps + am[node][other_node])
                visited[other_node] = False

    dfs(0, 0)

    return min_distance


def solution(filename: str) -> int:
    adjacency_matrix, node_positions = parse(filename)
    return solve(adjacency_matrix, 0, len(node_positions))


if __name__ == "__main__":
    print(solution("./input.txt"))  # 464
