package main

import (
	"fmt"
	"os"
	"strings"
)

var KEYPAD = [][]string{
	{".", ".", ".", ".", ".", ".", "."},
	{".", ".", ".", "1", ".", ".", "."},
	{".", ".", "2", "3", "4", ".", "."},
	{".", "5", "6", "7", "8", "9", "."},
	{".", ".", "A", "B", "C", ".", "."},
	{".", ".", ".", "D", ".", ".", "."},
	{".", ".", ".", ".", ".", ".", "."},
}

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func solve(instructions []string) string {
	codes := []string{}

	current_row := 3
	current_col := 1

	for _, row := range instructions {
		for _, direction := range row {
			switch direction {
			case 'U':
				new_row := current_row - 1
				if KEYPAD[new_row][current_col] != "." {
					current_row = new_row
				}

			case 'D':
				new_row := current_row + 1
				if KEYPAD[new_row][current_col] != "." {
					current_row = new_row
				}

			case 'L':
				new_col := current_col - 1
				if KEYPAD[current_row][new_col] != "." {
					current_col = new_col
				}

			case 'R':
				new_col := current_col + 1
				if KEYPAD[current_row][new_col] != "." {
					current_col = new_col
				}
			}
		}
		codes = append(codes, KEYPAD[current_row][current_col])
	}
	return strings.Join(codes, "")
}

func solution(filename string) string {
	instructions := parse(filename)
	return solve(instructions)
}

func main() {
	fmt.Println(solution("./example.txt")) // 5DB3
	fmt.Println(solution("./input.txt"))   // AC8C8
}
