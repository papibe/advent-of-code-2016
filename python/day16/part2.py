import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple, Iterable

INV: Dict[str, str] = {"0": "1", "1": "0"}
TAIL: Dict[str, str] = {
    "0": {
        "0": "1",
        "1": "0",
    },
    "1": {
        "0": "0",
        "1": "1",
    }
}
LAST: int = -1

def check_sum_first(data: List[str], pad: List[str], length: int) -> str:

    s_check = get_short_cs(data)
    ri_data = reverse_invert(data)
    s_ri_check = get_short_cs(ri_data)

    s_last: str = data[LAST]
    s_ri_last: str = INV[data[0]]

    loop = [[s_check, s_last, data], [s_ri_check, s_ri_last,ri_data]]

    pad_index: int = 0
    index: int = 0
    checksum: List[str] = []

    n: int = length // (len(data) + 1)

    for index in range(n):
        s, last, _ = loop[index % 2]
        checksum.extend(s)
        checksum.append(TAIL[last][pad[pad_index]])
        pad_index += 1

    diff: int = length - (len(data) + 1)*n

    _, _, s = loop[(index + 1) % 2]

    i = 0
    for _ in range(diff // 2):
        item, n_item = s[i], s[i + 1]
        checksum.append(TAIL[item][n_item])
        i += 2

    return checksum


def get_short_cs(data: List[str]) -> List[str]:
    check = []
    for i in range(0, len(data) - 1, 2):
        check.append(TAIL[data[i]][data[i + 1]])

    return check



def reverse_invert(s: List[str]) -> List[str]:
    output = []
    for index in range(len(s) - 1, -1, -1):
        output.append(INV[s[index]])

    return output


def check_sum(data: List[str], pad: List[str], length: int) -> str:

    data = check_sum_first(data, pad, length)

    checksum: List[str] = []

    counter: int = 0
    while True:
        counter += 1
        checksum: List[str] = []
        for index in range(0, len(data), 2):

            if data[index] == data[index + 1]:
                checksum.append("1")
            else:
                checksum.append("0")

        if len(checksum) % 2 != 0:
            break
        else:
            data = checksum

    return "".join(checksum)



def solve(puzzle_input: str, length: int) -> int:

    a: List[str] = list(puzzle_input)

    while len(a) < length:
        a_reversed: Iterable[str] = reversed(a)

        a.append("0")
        ri_a = []
        for char in a_reversed:
            a.append(INV[char])
            ri_a.append(INV[char])

    return a[:length]


def solution(puzzle_input: str, length: int) -> int:
    assert len(puzzle_input) % 2 == 1

    padding = solve("", length // (len(puzzle_input) + 1))

    return check_sum(puzzle_input, padding, length)

if __name__ == "__main__":
    result = solution("10001110011110000", 35651584)
    assert result ==  "01100111101101111"
    print(result)
