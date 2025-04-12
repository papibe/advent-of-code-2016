import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

from math import ceil

NO_PRESENTS: int = 0

class Node:
    def __init__(self, value: int, next_: "Node" = None, prev: "Node" = None) -> None:
        self.value: int = value
        self.next: "Node" = next_
        self.prev: "Node" = prev
        self.angle: float = 0.0


def solve(head: Node, n: int) -> int:

    player: Node = head

    original_number_of_players: int = n
    finished_round: bool = False
    processed = set()

    while n > 1:
        index: int = 0
        current = player
        if player.value in processed:
            break

        processed.add(player.value)
        # for _ in range(n):
        #     current.angle = index * (360 / n)
        #     current = current.next
        #     index += 1

        # current = player
        # for _ in range(n):
        #     print(current.value, current.angle)
        #     current = current.next
        # print()

        # current_angle: float = player.angle
        # angle_across: float = (current_angle + 180) % 360

        # print(f"{current_angle = }, {angle_across = }")

        # find
        # p: Node = player.prev
        # prev_index: int = 1
        # guess_index: int = ceil(angle_across / (360 / n))
        # while p.angle > angle_across:
        #     # print(p.value, p.angle)
        #     p = p.prev
        #     prev_index += 1

        counter = 0
        q: Node = player.prev
        # guess_index: int = ceil(angle_across / (360 / n))
        guess_index: int = ceil(180 / (360 / n))
        for _ in range(guess_index - 1):
            q = q.prev
            counter += 1


        # print(f"--------- {prev_index = } {guess_index = }")
        # assert prev_index == guess_index
        # assert p == q

        # eliminate p
        p = q
        prev = p.prev
        next_ = p.next
        prev.next = next_
        next_.prev = prev
        n -= 1

        # if n % 500 == 0:
        #     print(f"====> {player.value} takes {p.value}, {n}, {counter = }")

        player = player.next

        if finished_round:
            break

    remaining = []
    current = player
    for _ in range(n):
        remaining.append(player.value)
        player = player.next

    return remaining
    # return player.value



def create_players(n: int) -> Node:
    head: Node = Node(1)
    current: Node = head
    for index in range(2, n + 1):
        node: Node = Node(index)
        current.next = node
        node.prev = current
        current = node

    current.next = head
    head.prev = current

    return head

def solution(number_of_elves: int) -> int:
    players: Node = create_players(number_of_elves)

    # current = players
    # for _ in range(number_of_elves):
    #     print(current.value)
    #     current = current.next
    # print()

    # current = players
    # for _ in range(number_of_elves):
    #     print(current.value)
    #     current = current.prev
    # print()




    return solve(players, number_of_elves)


def josephus(n: int) -> int:
    if n == 1:
        return 1

    if n % 2 == 0:
        return 2 * josephus(n // 2) - 1
    else:
        return 2 * josephus(n // 2) + 1



if __name__ == "__main__":

    for n in range(1, 33 + 1):
        r = solution(n)
        j = josephus(n)
        # if r == 1:
        print(n, r,)
        # if r == j:
        #     # print(n, r, end='')
        #     print(" <----")
        # else:
        #     print("")

    # print(solution(5))  # 2
    # print(solution(3014387))  #
