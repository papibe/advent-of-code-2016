import pytest
from typing import List

from part1 import Instruction, Location, solve

r2 = Instruction("R", 2)
l3 = Instruction("L", 3)
r5 = Instruction("R", 5)
l5 = Instruction("L", 5)
r3 = Instruction("R", 3)

@pytest.mark.parametrize(
    "instructions,expected",
    [
        ([r2, l3], 5),
        ([r2, r2, r2], 2),
        ([r5, l5, r5, r3], 12),
    ],
    ids=[
        "[r2, l3]_should_be_5",
        "[r2, r2, r2]_should_be_2",
        "[r5, l5, r5, r3]_should_be_12",
    ],
)
def test_part1(instructions: List[Instruction], expected: int) -> None:
    result: int = solve(instructions, Location())
    assert result == expected, f"got {result}, needs {expected}"
