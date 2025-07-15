import re
from dataclasses import dataclass
from typing import List, Match, Optional


@dataclass
class Node:
    name: str
    used: int
    avail: int


def parse(filename: str) -> List[Node]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    re_node: str = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"

    nodes: List[Node] = []

    for i in range(2, len(data)):
        line: str = data[i]
        matches: Optional[Match[str]] = re.match(re_node, line)

        assert matches is not None

        x: str = matches.group(1)
        y: str = matches.group(2)
        _size: int = int(matches.group(3))
        used: int = int(matches.group(4))
        avail: int = int(matches.group(5))
        _percentage_used: int = int(matches.group(6))
        nodes.append(Node(f"{x},{y}", used, avail))

    return nodes


def are_viable(a: Node, b: Node) -> bool:
    if a.used == 0:
        return False

    if a == b:
        return False

    if a.used <= b.avail:
        return True

    return False


def solve(nodes: List[Node]) -> int:
    viable_pairs_count: int = 0
    n: int = len(nodes)

    for i in range(n):
        for j in range(i + 1, n):
            node1: Node = nodes[i]
            node2: Node = nodes[j]

            if are_viable(node1, node2):
                viable_pairs_count += 1

            if are_viable(node2, node1):
                viable_pairs_count += 1

    return viable_pairs_count


def solution(filename: str) -> int:
    data: List[Node] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 903
