package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	CPY = "cpy"
	INC = "inc"
	DEC = "dec"
	JNZ = "jnz"
	TGL = "tgl"
)

type Instruction struct {
	instruction string
	param1      string
	param2      string
}

func is_alpha(word string) bool {
	return regexp.MustCompile(`^[a-zA-Z]*$`).MatchString(word)
}

func parse(filename string) ([]Instruction, map[string]int) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}

	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")

	// parse program
	program := []Instruction{}
	for _, line := range lines {
		tokens := strings.Split(line, " ")

		param := ""
		if len(tokens) == 3 {
			param = tokens[2]
		}
		instruction := Instruction{tokens[0], tokens[1], param}
		program = append(program, instruction)
	}

	// create registers
	registers := make(map[string]int)
	for _, register := range []string{"a", "b", "c", "d"} {
		registers[register] = 0
	}

	return program, registers

}

func run(program []Instruction, registers map[string]int) int {
	pointer := 0
	var value int

	for pointer < len(program) {

		instr := program[pointer]

		switch instr.instruction {
		case CPY:
			if is_alpha(instr.param1) {
				value = registers[instr.param1]
			} else {
				value, _ = strconv.Atoi(instr.param1)
			}
			if is_alpha(instr.param2) {
				registers[instr.param2] = value
			}

		case INC:
			if is_alpha(instr.param1) && instr.param2 == "" {
				registers[instr.param1] += 1
			}

		case DEC:
			if is_alpha(instr.param1) && instr.param2 == "" {
				registers[instr.param1] -= 1
			}

		case JNZ:
			var x int
			if is_alpha(instr.param1) {
				x = registers[instr.param1]
			} else {
				x, _ = strconv.Atoi(instr.param1)
			}
			if is_alpha(instr.param2) {
				value = registers[instr.param2]
			} else {
				value, _ = strconv.Atoi(instr.param2)
			}
			if x > 0 {
				pointer += value
				continue
			}
		case TGL:
			if is_alpha(instr.param1) {
				value = registers[instr.param1]
			} else {
				value, _ = strconv.Atoi(instr.param1)
			}
			toggle_pointer := pointer + value
			if toggle_pointer < len(program) {
				toggle_instruction := program[toggle_pointer]

				is_one_argument := toggle_instruction.param2 == ""

				if is_one_argument {
					if toggle_instruction.instruction == INC {
						program[toggle_pointer] = Instruction{DEC, toggle_instruction.param1, toggle_instruction.param2}
					} else {
						program[toggle_pointer] = Instruction{INC, toggle_instruction.param1, toggle_instruction.param2}
					}

				} else { // two params
					if toggle_instruction.instruction == JNZ {
						program[toggle_pointer] = Instruction{CPY, toggle_instruction.param1, toggle_instruction.param2}
					} else {
						program[toggle_pointer] = Instruction{JNZ, toggle_instruction.param1, toggle_instruction.param2}
					}
				}
			}
		}
		pointer++
	}
	return registers["a"]
}

func solution(filename string) int {
	program, registers := parse(filename)
	registers["a"] = 7
	return run(program, registers)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3
	fmt.Println(solution("./input.txt"))   // 10152
}
