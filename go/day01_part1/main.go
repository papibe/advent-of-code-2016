package main

import (
	"fmt"
	"os"
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

func parse(filename string) []Instruction {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	instructions := []Instruction{}
	lines := strings.Trim(string(data), "\n")

	for _, line := range strings.Split(lines, ", ") {
		direction := string(line[0])
		steps, _ := strconv.Atoi(line[1:])
		instructions = append(instructions, Instruction{direction, steps})
	}

	return instructions
}

func solve(instructions []Instruction, location Location) int {
	for _, instruction := range instructions {
		location.move(instruction)
	}
	return location.get_distance()
}

func solution(filename string) int {
	instructions := parse(filename)
	location := Location{0, 0, Direction{-1, 0}}
	return solve(instructions, location)
}

func main() {
	fmt.Println(solution("./input.txt"))
}
