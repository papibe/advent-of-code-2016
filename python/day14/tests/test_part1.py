import pytest
from typing import List
from part1 import md5_hash, count_repetitions


@pytest.mark.parametrize(
    "source,expected",
    [
        ("abc18", "cc38887a5"),
        ("abc39", "eee"),
        ("abc816", "eeeee"),
        ("abc92", "999"),
        ("abc200", "99999"),
    ],
    ids=[
        "abc18_contains_cc38887a5",
        "abc39_contains_eee",
        "abc816_contains_eeeee",
        "abc92_contains_999",
        "abc200_contains_99999",
    ],
)
def test_part_mdhash(source: str, expected: int) -> None:
    result: int = md5_hash(source)
    assert expected in result, f"got {result}, needs {expected}"


@pytest.mark.parametrize(
    "source,found,char,fives",
    [
        ("abc18", True, "8", []),
        ("abc39", True, "e", []),
        ("abc816", True, "e", ["e"]),
        ("abc92", True, "9", []),
        ("abc200", True, "9", ["9"]),
    ],
)
def test_part_count_repetitions(
    source: str, found: bool, char: str, fives: List[int]
) -> None:
    hash_: int = md5_hash(source)
    found_result, found_char, found_fives = count_repetitions(hash_)

    assert found_result == found, f"got {found_result}, needs {found}"
    assert found_char == char, f"got {found_char}, needs {char}"
    assert found_fives == fives, f"got {found_fives}, needs {fives}"
