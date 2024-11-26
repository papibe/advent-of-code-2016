import pytest
from typing import List
from part2 import stretch_hash, count_repetitions


@pytest.mark.parametrize(
    "source,times,expected",
    [
        ("abc0", 0, "577571be4de9dcce85a041ba0410f29f"),
        ("abc0", 1, "eec80a0c92dc8a0777c619d9bb51e910"),
        ("abc0", 2, "16062ce768787384c81fe17a7a60c7e3"),
        ("abc0", 2016, "a107ff634856bb300138cac6568c0f24"),
    ],
    ids=[
        "abc18_hashed_1_is_577571be4de9dcce85a041ba0410f29f",
        "abc18_hashed_2_is_eec80a0c92dc8a0777c619d9bb51e910",
        "abc18_hashed_3_is_16062ce768787384c81fe17a7a60c7e3",
        "abc18_hashed_2017_is_a107ff634856bb300138cac6568c0f24",
    ],
)
def test_part_stretch_hash(source: str, times: int, expected: int) -> None:
    result: int = stretch_hash(source, times)
    assert expected in result, f"got {result}, needs {expected}"


@pytest.mark.parametrize(
    "source,found,char,fives",
    [
        ("abc5", True, "2", []),
        ("abc10", True, "e", []),
        ("abc89", True, "e", ["e"]),
        ("abc22551", True, "f", []),
        ("abc22859", True, "f", ["f"]),
    ],
)
def test_part_count_repetitions(
    source: str, found: bool, char: str, fives: List[int]
) -> None:
    hash_: int = stretch_hash(source, 2016)
    found_result, found_char, found_fives = count_repetitions(hash_)

    assert found_result == found, f"got {found_result}, needs {found}"
    assert found_char == char, f"got {found_char}, needs {char}"
    assert found_fives == fives, f"got {found_fives}, needs {fives}"
