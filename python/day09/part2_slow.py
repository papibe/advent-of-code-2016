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


def solve(omarkers: List[Marker], current_length: int) -> int:
    next_length: int = 0
    position: int = 0
    cycle: int = 0

    markers = []
    for i, m in enumerate(omarkers):
        markers.append(i)

    marker_positions = []
    for i, m in enumerate(omarkers):
        marker_positions.append(m.position)

    while len(markers) > 0:
        marker_index: int = 0
        position: int = 0
        next_length: int = 0
        next_markers: List[Marker] = []
        next_marker_positions: List[Marker] = []

        cycle += 1

        # print()
        # print(f"At start cycle: {cycle}")
        # for m in markers:
        #     print("    ", m)

        while marker_index < len(markers):
            marker: Marker = omarkers[markers[marker_index]]

            # print(f"working with marker {marker_index}: {marker}")

            marker_position = marker_positions[marker_index]

            next_length += marker_position - position

            # print(f"{next_length = }")

            size: int = marker.size
            times: int = marker.times

            sequence_start: int = marker_position + marker.length
            sequence_end: int = sequence_start + size

            # print(f"{sequence_start = }, {sequence_end = }")
            # print()

            for repeat in range(times):
                i: int = marker_index + 1

                while i < len(markers) and marker_positions[i] < sequence_end:
                    next_markers.append(markers[i])
                    new_position = (
                        next_length
                        + (marker_positions[i] - sequence_start)
                        + size * repeat
                    )
                    next_marker_positions.append(new_position)

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
        del marker_positions

        markers = next_markers
        marker_positions = next_marker_positions

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
    # it takes 1m 35s
    print(solution("./input.txt"))  # 10774309173
