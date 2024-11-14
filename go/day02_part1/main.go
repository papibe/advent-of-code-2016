package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var KEYPAD = [][]string{
	{"1", "2", "3"},
	{"4", "5", "6"},
	{"7", "8", "9"},
}

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func solve(instructions []string) int {
	codes := []string{}

	current_row := 1
	current_col := 1

	for _, row := range instructions {
		for _, direction := range row {
			switch direction {
			case 'U':
				new_row := current_row - 1
				if new_row >= 0 {
					current_row = new_row
				}

			case 'D':
				new_row := current_row + 1
				if new_row < 3 {
					current_row = new_row
				}

			case 'L':
				new_col := current_col - 1
				if new_col >= 0 {
					current_col = new_col
				}

			case 'R':
				new_col := current_col + 1
				if new_col < 3 {
					current_col = new_col
				}
			}
		}
		codes = append(codes, KEYPAD[current_row][current_col])
	}
	code, _ := strconv.Atoi(strings.Join(codes, ""))
	return code
}

func solution(filename string) int {
	instructions := parse(filename)
	return solve(instructions)
}

func main() {
	fmt.Println(solution("./example.txt")) // 1985
	fmt.Println(solution("./input.txt"))   // 78293
}
