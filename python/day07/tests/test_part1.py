import pytest

from part1 import got_abba, supports_tls


@pytest.mark.parametrize(
    "word,expected",
    [
        ("abba", True),
        ("xyyx", True),
        ("yxxy", True),
        ("aaaa", False),
        ("bddb", True),
        ("ioxxoj", True),
        ("iasoxxo", True),
        ("oxxoias", True),
        ("123", False),
    ],
    ids=[
        "abba_should_be_True",
        "xyyx_should_be_True",
        "yxxy_should_be_True",
        "aaaa_should_be_False",
        "bddb_should_be_True",
        "ioxxoj_should_be_True",
        "iasoxxo_should_be_True",
        "oxxoias_should_be_True",
        "123_should_be_False",
    ],
)
def test_part1_got_abba(word: str, expected: int) -> None:
    result: int = got_abba(word)
    assert result == expected, f"got {result}, needs {expected}"


@pytest.mark.parametrize(
    "ip,expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
    ids=[
        "abba[mnop]qrst_should_be_True",
        "abcd[bddb]xyyx_should_be_False",
        "aaaa[qwer]tyui_should_be_False",
        "ioxxoj[asdfgh]zxcvbn_should_be_True",
    ],
)
def test_part1_supports_tls(ip: str, expected: int) -> None:
    result: int = supports_tls(ip)
    assert result == expected, f"got {result}, needs {expected}"
