import pytest

from part2 import supports_ssl


@pytest.mark.parametrize(
    "ip,expected",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
    ids=[
        "aba[bab]xyz_should_be_True",
        "xyx[xyx]xyx_should_be_False",
        "aaa[kek]eke_should_be_True",
        "zazbz[bzb]cdb_should_be_True",
    ],
)
def test_part1_supports_ssl(ip: str, expected: bool) -> None:
    result: bool = supports_ssl(ip)
    assert result == expected, f"got {result}, needs {expected}"
