package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Instruction struct {
	direction string
	steps     int
}

type Direction struct {
	row int
	col int
}

func (d *Direction) rotate(direction string) {
	prev_row := (*d).row
	prev_col := (*d).col

	if direction == "R" {
		(*d).row = prev_col
		(*d).col = -prev_row
	} else {
		(*d).row = -prev_col
		(*d).col = prev_row
	}
}

type Location struct {
	row int
	col int
	dir Direction
}

func (l *Location) move(instruction Instruction) {
	(*l).dir.rotate(instruction.direction)

	(*l).row += instruction.steps * (*l).dir.row
	(*l).col += instruction.steps * (*l).dir.col
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func (l *Location) get_distance() int {
	return abs(l.row) + abs(l.col)
}

func parse(filename string) string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Trim(string(data), "\n")
}

func solve(sequence string) int {
	output_len := 0
	index := 0

	marker_regex := regexp.MustCompile(`^\((\d+)x(\d+)\)`)

	for len(sequence) > 0 {
		matches := marker_regex.FindStringSubmatch(sequence)

		if len(matches) > 0 {
			amount, _ := strconv.Atoi(matches[1])
			times, _ := strconv.Atoi(matches[2])

			index = len(matches[0])

			output_len += times * amount
			index += amount

		} else {
			index = 1
			output_len++
		}
		sequence = sequence[index:]
	}
	return output_len
}

func solution(filename string) int {
	sequence := parse(filename)
	return solve(sequence)
}

func main() {
	fmt.Println(solution("./input.txt"))
}
