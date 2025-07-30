package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

const (
	CPY = "cpy"
	INC = "inc"
	DEC = "dec"
	JNZ = "jnz"
	TGL = "tgl"
	OUT = "out"
)

type StateKey struct {
	pointer    int
	value      int
	register_a int
	register_b int
	register_c int
	register_d int
}

type Instruction struct {
	instruction string
	param1      string
	param2      string
}

func is_alpha(word string) bool {
	letter := rune(word[0])
	return unicode.IsLetter(letter)
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

func run(program *[]Instruction, registers *map[string]int) bool {
	pointer := 0
	var value int
	var x int
	previous := 1
	counter := 0
	seen := NewSet[StateKey]()

	for pointer < len(*program) {

		instr := (*program)[pointer]

		switch instr.instruction {
		case CPY:
			if is_alpha(instr.param1) {
				value = (*registers)[instr.param1]
			} else {
				value, _ = strconv.Atoi(instr.param1)
			}
			if is_alpha(instr.param2) {
				(*registers)[instr.param2] = value
			}

		case INC:
			if is_alpha(instr.param1) && instr.param2 == "" {
				(*registers)[instr.param1] += 1
			}

		case DEC:
			if is_alpha(instr.param1) && instr.param2 == "" {
				(*registers)[instr.param1] -= 1
			}

		case JNZ:
			// var x int
			if is_alpha(instr.param1) {
				x = (*registers)[instr.param1]
			} else {
				x, _ = strconv.Atoi(instr.param1)
			}
			if is_alpha(instr.param2) {
				value = (*registers)[instr.param2]
			} else {
				value, _ = strconv.Atoi(instr.param2)
			}
			if x > 0 {
				pointer += value
				continue
			}
		case OUT:
			counter++
			if instr.param2 == "" {
				if is_alpha(instr.param1) {
					value = (*registers)[instr.param1]
				} else {
					value, _ = strconv.Atoi(instr.param1)
				}
			}
			if previous == 1 && value == 1 {
				return false
			}
			if previous == 0 && value == 0 {
				return false
			}
			state_key := StateKey{
				pointer,
				value,
				(*registers)["a"],
				(*registers)["b"],
				(*registers)["c"],
				(*registers)["d"],
			}

			if seen.contains(state_key) {
				return true
			}
			seen.add(state_key)
			previous = value
		}
		pointer++
	}
	return false
}

func solution(filename string) int {
	program, registers := parse(filename)
	for n := range 1000 {
		registers["a"] = n
		if run(&program, &registers) {
			return n
		}
	}
	return -1
}

func main() {
	fmt.Println(solution("./input.txt")) // 189
}
