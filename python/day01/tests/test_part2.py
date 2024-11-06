import pytest
from typing import List

from part2 import Instruction, Location, solve

r8 = Instruction("R", 8)
r4 = Instruction("R", 4)

@pytest.mark.parametrize(
    "instructions,expected",
    [
        ([r8, r4, r4, r8], 4),
    ],
    ids=[
        "[r8, r4, r4, r8]_should_be_4",
    ],
)
def test_part2(instructions: List[Instruction], expected: int) -> None:
    result: int = solve(instructions, Location())
    assert result == expected, f"got {result}, needs {expected}"
