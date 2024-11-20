from collections import namedtuple
from typing import Dict, List, Tuple

# type definitions
Instruction = namedtuple("Instruction", ["instruction", "param1", "param2"])
Registers = Dict[str, int]


class INSTR:
    CPY: str = "cpy"
    INC: str = "inc"
    DEC: str = "dec"
    JNZ: str = "jnz"


def parse(filename: str) -> Tuple[List[Instruction], Registers]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    # parse program
    program: List[Instruction] = []
    for line in data:
        parsed: List[str] = line.split()
        instuction: Instruction = Instruction(
            instruction=parsed[0],
            param1=parsed[1],
            param2=parsed[2] if len(parsed) == 3 else "",
        )
        program.append(instuction)

    # create registers
    registers: Dict[str, int] = {}
    for register in "abcd":
        registers[register] = 0

    return program, registers


def run(program: List[Instruction], registers: Dict[str, int]) -> int:
    pointer: int = 0
    value: int

    while pointer < len(program):
        instr: Instruction = program[pointer]

        match instr.instruction:
            case INSTR.CPY:
                if instr.param1.isalpha():
                    value = registers[instr.param1]
                else:
                    value = int(instr.param1)
                registers[instr.param2] = value

            case INSTR.INC:
                registers[instr.param1] += 1

            case INSTR.DEC:
                registers[instr.param1] -= 1

            case INSTR.JNZ:
                x: int
                if instr.param1.isalpha():
                    x = registers[instr.param1]
                else:
                    x = int(instr.param1)

                if instr.param2.isalpha():
                    value = registers[instr.param2]
                else:
                    value = int(instr.param2)

                if x > 0:
                    pointer += value
                    continue

        pointer += 1

    return registers["a"]


def solution(filename: str) -> int:
    program, registers = parse(filename)
    registers["c"] = 1
    return run(program, registers)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 9227647
