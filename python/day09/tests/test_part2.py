import pytest

from part2 import parse_markers, solve


# @pytest.mark.parametrize(
#     "sequence,expected",
#     [
#         ("ADVENT", 6),
#         ("A(1x5)BC", 7),
#         ("(3x3)XYZ", 9),
#         ("A(2x2)BCD(2x2)EFG", 11),
#         ("(6x1)(1x3)A", 6),
#         ("X(8x2)(3x3)ABCY", 18),
#     ],
#     # ids=[
#     #     "aa_bb_cc_dd_ee_should_be_True",
#     #     "aa_bb_cc_dd_aa_should_be_False",
#     #     "aa_bb_cc_dd_aaa_should_be_True",
#     # ],
# )
# def test_part1(sequence: str, expected: int) -> None:
#     markers, length = parse_markers(sequence)
#     result: int = solve(markers, length)

#     assert result == expected, f"got {result}, needs {expected}"


@pytest.mark.parametrize(
    "sequence,expected",
    [
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
    # ids=[
    #     "aa_bb_cc_dd_ee_should_be_True",
    #     "aa_bb_cc_dd_aa_should_be_False",
    #     "aa_bb_cc_dd_aaa_should_be_True",
    # ],
)
def test_part1(sequence: str, expected: int) -> None:
    markers, length = parse_markers(sequence)
    result: int = solve(markers, length)
    assert result == expected, f"got {result}, needs {expected}"