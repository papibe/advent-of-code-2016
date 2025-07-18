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
    TGL: str = "tgl"


def parse(filename: str) -> Tuple[List[Instruction], Registers]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    # parse program
    program: List[Instruction] = []
    for line in data:
        parsed: List[str] = line.split()
        instruction: Instruction = Instruction(
            instruction=parsed[0],
            param1=parsed[1],
            param2=parsed[2] if len(parsed) == 3 else "",
        )
        program.append(instruction)

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

                if instr.param2.isalpha():
                    registers[instr.param2] = value

            case INSTR.INC:
                if instr.param1.isalpha() and instr.param2 == "":
                    registers[instr.param1] += 1

            case INSTR.DEC:
                if instr.param1.isalpha() and instr.param2 == "":
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

            case INSTR.TGL:
                if instr.param1.isalpha():
                    value = registers[instr.param1]
                else:
                    value = int(instr.param1)

                toggle_pointer: int = pointer + value
                if toggle_pointer < len(program):

                    toggle_instruction: Instruction = program[toggle_pointer]

                    is_one_argument: bool = toggle_instruction.param2 == ""

                    if is_one_argument:
                        if toggle_instruction.instruction == INSTR.INC:
                            program[toggle_pointer] = Instruction(
                                INSTR.DEC,
                                toggle_instruction.param1,
                                toggle_instruction.param2,
                            )
                        else:
                            program[toggle_pointer] = Instruction(
                                INSTR.INC,
                                toggle_instruction.param1,
                                toggle_instruction.param2,
                            )

                    else:  # 2 params
                        if toggle_instruction.instruction == INSTR.JNZ:
                            program[toggle_pointer] = Instruction(
                                INSTR.CPY,
                                toggle_instruction.param1,
                                toggle_instruction.param2,
                            )
                        else:
                            program[toggle_pointer] = Instruction(
                                INSTR.JNZ,
                                toggle_instruction.param1,
                                toggle_instruction.param2,
                            )

        pointer += 1
        assert len(registers) == 4

    return registers["a"]


def solution(filename: str) -> int:
    program, registers = parse(filename)
    registers["a"] = 7
    return run(program, registers)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3
    print(solution("./input.txt"))  # 10152
