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
    OUT: str = "out"


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
    previous = 1
    counter = 0
    seen = set()

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

            case INSTR.OUT:
                counter += 1
                if instr.param2 == "":
                    if instr.param1.isalpha():
                        value = registers[instr.param1]
                    else:
                        value = int(instr.param1)

                if previous == 1 and value == 1:
                    return False
                if previous == 0 and value == 0:
                    return False

                state_key = (
                    pointer,
                    value,
                    registers["a"],
                    registers["b"],
                    registers["c"],
                    registers["d"],
                )

                if state_key in seen:
                    return True

                seen.add(state_key)

                previous = value
                # if counter > 100:
                #     return True

        pointer += 1

    return False


def solution(filename: str) -> int:
    program, registers = parse(filename)
    for n in range(1_000):
        registers["a"] = n
        good = run(program, registers)
        if good:
            return n
    return -1


if __name__ == "__main__":
    print(solution("./input.txt"))  # 189
