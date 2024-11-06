import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

@dataclass
class Room:
    name: str
    raw_name: str
    sector: int
    checksum: str

    def is_real(self) -> bool:
        # get frequency
        frequency: Dict[str, int] = {}
        for char in self.name:
            frequency[char] = frequency.get(char, 0) + 1

        # bucket sort
        bucket: Dict[int, List[str]] = {}
        for k, v in frequency.items():
            if v not in bucket:
                bucket[v] = []
            bucket[v].append(k)

        # sort alphabetically
        for k, v in bucket.items():
            v.sort()

        # sort frequencies
        sorted_freqs: List[str] = sorted(bucket, reverse=True)

        # calculate long checksum
        checksum: List[str] = []
        for freq in sorted_freqs:
            checksum.extend(bucket[freq])

        if "".join(checksum[:5]) == self.checksum:
            return True

        return False

    def decrypt(self) -> str:
        plain: List[str] = []
        for char in self.raw_name:
            # print(char)
            if char == "-":
                plain_char: str = " "
            else:
                plain_value = (ord(char) - ord("a") + self.sector) % 26 + ord("a")
                plain_char: str = chr(plain_value)
            plain.append(plain_char)

        return "".join(plain)

def parse(filename: str) -> List[Room]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rooms: List[Room] = []

    for line in data:
        tmp: List[str] = line.split(r"[")
        checksum: str = tmp[-1][:-1]

        tmp2: List[str] = tmp[0].split("-")
        sector: int = int(tmp2[-1])
        name: str = "".join(tmp2[:-1])
        raw_name: str = "-".join(tmp2[:-1])

        rooms.append(Room(name, raw_name, sector, checksum))

    return rooms


def solve(rooms: List[Room]) -> int:
    sector_sum: int = 0

    for room in rooms:
        if room.is_real():
            sector_sum += room.sector
            if "northpole object storage" == room.decrypt():
                return room.sector

    return -1


def solution(filename: str) -> int:
    rooms: List[Room] = parse(filename)
    return solve(rooms)


if __name__ == "__main__":
    # print(solution("./example2.txt"))  # 0
    print(solution("./input.txt"))  # 0
