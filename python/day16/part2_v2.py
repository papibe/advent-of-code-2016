import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

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

INV: Dict[str, str] = {"0": "1", "1": "0"}

def check_sum(data: List[str]) -> str:

    checksum: List[str] = []

    while True:
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


def initial_cs(
    s: List[str], checks: Dict[str, Dict[str, str]], n: int, length: int
) -> List[str]:
    output: List[str] = []
    size: int = 0
    i: int = 0


    while True:
        current: str = s[i]
        # print(f"{size = }")
        # print(f"{size + n + 1 = }")
        if size + n + 1 <= length:
            next_: str = s[i + 1]
            output.extend(checks[current][next_])
            size += n + 1
        else:
            # print("here")
            j: int = 0
            w = checks[current][current]
            # for j in range(0, (length - size) // 2 + 1, 2):
            while size < length:
                if w[j] == w[j + 1]:
                    output.append("1")
                else:
                    output.append("0")
                size += 2
            break

        # print(output, i, size, l, length)
        i += 2

    # print(f"{output = }")

    return "".join(output)




def short_cs(data: List[str]) -> List[str]:
    check = []
    for index in range(0, len(data) - 1, 2):
        check.append(TAIL[data[index]][data[index + 1]])

    return check

def reverse_invert(s: List[str]) -> List[str]:
    output = []
    for index in range(len(s) - 1, -1, -1):
        output.append(INV[s[index]])

    return output, "".join(output)


def dfs_ri(start: int, end: int, n: int, l: int) -> List[str]:
    middle: int = (end - start + 1) // 2  + start   # 1

    # print(f"left {start = }, {end = }, {n = }, {l = }")
    # print(f"left {middle = }")


    right_side_len: int = middle - start
    if right_side_len == n:
        # print("left: got there")
        # right_side = checks["r1"]["1"]
        right_side = ["s"]
    else:
        right_side = dfs_right(start, middle - 1, n, l)


    left_side_len: int = end - middle
    if left_side_len == n:
        left_side = ["s_ri"]
    else:
        # left_side: int = dfs_right(middle + 1, end, n, checks, l)
        left_side: int = dfs_ri(middle + 1, end, n, l)

    output: List[str] = right_side
    output.append("1")
    output.extend(left_side)
    return output


def dfs_right(start: int, end: int, n: int, l: int) -> List[str]:
    middle: int = (end - start + 1) // 2  + start   # 0

    # print(f"right {start = }, {end = }, {n = }, {l = }")
    # print(f"right {middle = }")

    right_side_len: int = middle - start
    if right_side_len == n:
        # print("right: got there")
        # right_side = checks["right"]["0"]
        right_side = ["s"]
    else:
        right_side = dfs_right(start, middle - 1, n, l)

    left_side_len: int = end - middle
    if left_side_len == n:
        left_side = ["s_ri"]
    else:
        left_side: int = dfs_ri(middle + 1, end, n, l)

    output: List[str] = right_side
    output.append("0")
    output.extend(left_side)
    return output



def solution(puzzle_input: str, length: int) -> int:
    # pre-calculated checksums
    checks: Dict[str, Dict[str, str]] = {}
    checks["s"] = {
        "0": short_cs(puzzle_input + "0"),
        "1": short_cs(puzzle_input + "1"),
        "s": puzzle_input,
    }

    _, ri_data = reverse_invert(puzzle_input)
    checks["s_ri"] = {
        "0": short_cs(ri_data + "0"),
        "1": short_cs(ri_data + "1"),
        "s_ri": ri_data,
    }
    n: int = len(puzzle_input)

    for k in range(1, 100):
        l = (2**k) * n + (2**k - 1)
        # print(f"{k = }, {l  = }, {length = }")
        if  l >= length:
            break

    assert l >= length

    # print(f"{k = }", l)


    base: List[str] = dfs_right(0, l - 1, n, length)

    # print(base)
    # largo = 0
    # for item in base_cs:
    #     if item == "s" or item == "s_ri":
    #         largo += n
    #     elif item == "0" or item == "1":
    #         largo += 1
    #     else:
    #         raise ValueError("what?")

    # print(f"{largo = }")

    base_cs = initial_cs(base, checks, n, length)

    # print(base_cs)
    return check_sum(base_cs)


if __name__ == "__main__":
    # result = solution("10000", 20)
    # print(result)
    # assert result == "01100"

    # result = solution("10001110011110000", 272)
    # print(result)
    # assert result == "10010101010011101"

    result = solution("10001110011110000", 35651584)
    assert result ==  "01100111101101111"
    print(result)

