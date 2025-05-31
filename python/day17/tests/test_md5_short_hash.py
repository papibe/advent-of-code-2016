import pytest

from md5_hash import md5_short_hash


@pytest.mark.parametrize(
    "string,expected",
    [
        ("hijkl", "ced9"),
        ("hijklD", "f2bc"),
        ("hijklDR", "5745"),
        ("hijklDU", "528e"),
    ],
    ids=[
        "hijkl_should_be_ced9",
        "hijklD_should_be_f2bc",
        "hijklDR_should_be_5745",
        "hijklDU_should_be_528e",
    ],
)
def test_md5_short_hash(string: str, expected: str) -> None:
    result: str = md5_short_hash(string)
    assert result == expected, f"got {result}, needs {expected}"
