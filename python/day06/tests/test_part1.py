from typing import List

from part1 import solve

example: List[str] = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar",
]

expected: str = "easter"


def test_example1_data_should_be_easter(
    example: List[str] = example, expected: str = expected
) -> None:
    result: str = solve(example)
    assert result == expected, f"got {result}, needs {expected}"
