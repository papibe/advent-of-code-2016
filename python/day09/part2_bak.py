import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

@dataclass
class Marker:
    size: int
    times: int
    length: int
    position: int

    def copyi(self, position: int) -> "Marker":
        return Marker(self.size, self.times, self.length, position)

    def __repr__(self):
        return f"({self.size}x{self.times})[{self.position}]"


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip()
    return data


def parse_markers(data: str) -> Tuple[List[Marker], int]:

    marker_regex: str = r"\((\d+)x(\d+)\)"

    markers: List[Marker] = []

    for match_ in re.finditer(marker_regex, data):
        size: int = int(match_.group(1))
        times: int = int(match_.group(2))

        markers.append(Marker(size, times, len(match_.group(0)), match_.start()))

    return markers, len(data)


def solve(markers: List[Marker], current_length: int) -> int:
    next_length: int = 0
    position: int = 0
    cycle: int = 0

    while len(markers) > 0:
        marker_index: int = 0
        position: int = 0
        next_length: int = 0
        next_markers: List[Marker] = []

        cycle += 1

        # print()
        # print(f"At start cycle: {cycle}")
        # for m in markers:
        #     print("    ", m)


        while marker_index < len(markers):
            marker: Marker = markers[marker_index]

            # print(f"working with marker {marker_index}: {marker}")

            next_length += (marker.position - position)

            # print(f"{next_length = }")

            size: int = marker.size
            times: int = marker.times

            sequence_start: int = marker.position + marker.length
            sequence_end: int = sequence_start + size

            # print(f"{sequence_start = }, {sequence_end = }")
            # print()

            for repeat in range(times):
                i: int = marker_index + 1

                while i < len(markers) and markers[i].position < sequence_end:
                    new_marker: Marker = (
                        markers[i].copyi(
                            next_length + (markers[i].position - sequence_start) + size * repeat
                        )
                    )
                    next_markers.append(new_marker)

                    # print(markers[i], "--->",new_marker)

                    i += 1

            marker_index = i
            position = sequence_start + size
            next_length += size * times

            # print(f"{marker_index = }")
            # print(f"{position = }")
            # print(f"{next_length = }")
            # print()

        # print()
        # print("======= end cycle")
        # print(f"{current_length = }")

        if position == current_length:
            pass
        elif position < current_length:
            next_length += current_length - position
        else:
            print("WTF")

        # print(f"adjusted {next_length = }")

        current_length = next_length
        del markers
        markers = next_markers

        print(current_length, len(markers))

        # print("--markers--")
        # for m in markers:
        #     print("\t", m)

        # break


    return current_length


def solution(filename: str) -> int:
    content: str = parse(filename)
    markers, length = parse_markers(content)
    # print("--markers--")
    # for m in markers:
    #     print("\t", m)

    print(length, len(markers))

    return solve(markers, length)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 0
