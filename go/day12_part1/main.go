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
			registers[instr.param2] = value

		case INC:
			registers[instr.param1] += 1

		case DEC:
			registers[instr.param1] -= 1

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
		}
		pointer++

	}

	return registers["a"]
}

func solution(filename string) int {
	program, registers := parse(filename)
	return run(program, registers)
}

func main() {
	fmt.Println(solution("./example.txt")) // 42
	fmt.Println(solution("./input.txt"))   // 317993
}
