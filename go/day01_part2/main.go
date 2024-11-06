package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Position struct {
	row int
	col int
}

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

func (l *Location) move(amount int) Position {
	(*l).row += amount * (*l).dir.row
	(*l).col += amount * (*l).dir.col

	return Position{l.row, l.col}
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
	visited := make(map[Position]bool)
	visited[Position{0, 0}] = true

	for _, instruction := range instructions {
		location.dir.rotate(instruction.direction)

		for range instruction.steps {
			position := location.move(1)

			_, is_visited := visited[position]
			if is_visited {
				return location.get_distance()
			}

			visited[position] = true
		}
	}
	return -1
}

func solution(filename string) int {
	instructions := parse(filename)
	location := Location{0, 0, Direction{-1, 0}}
	return solve(instructions, location)
}

func main() {
	fmt.Println(solution("./input.txt"))
}
