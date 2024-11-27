package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type InstructionType string

const (
	RECT    InstructionType = "r"
	ROT_ROW InstructionType = "rr"
	ROT_COL InstructionType = "rc"
)

type Instruction struct {
	type_ InstructionType
	a     int
	b     int
}

type Display struct {
	grid [][]string
	rows int
	cols int
}

func NewDisplay(rows, cols int) *Display {
	grid := make([][]string, rows)
	for i, _ := range grid {
		grid[i] = make([]string, cols)
		for j, _ := range grid[i] {
			grid[i][j] = "."
		}
	}
	return &Display{
		grid: grid,
		rows: rows,
		cols: cols,
	}
}

func (d *Display) rect(a, b int) {
	cols := a
	rows := b

	for row := range rows {
		for col := range cols {
			d.grid[row][col] = "#"
		}
	}
}

func (d *Display) rot_row(a, b int) {
	row := a
	shift := b

	// copy original row
	original_row := make([]string, d.cols)
	for col := range d.cols {
		original_row[col] = d.grid[row][col]
	}

	// shift row
	for col := range d.cols {
		d.grid[row][(col+shift)%d.cols] = original_row[col]
	}
}

func (d *Display) rot_col(a, b int) {
	col := a
	shift := b

	// copy original col
	original_col := make([]string, d.rows)
	for row := range d.rows {
		original_col[row] = d.grid[row][col]
	}

	// shift col
	for row := range d.rows {
		d.grid[(row+shift)%d.rows][col] = original_col[row]
	}
}

func (d *Display) count() int {
	counter := 0
	for row := range d.rows {
		for col := range d.cols {
			if d.grid[row][col] == "#" {
				counter++
			}
		}
	}
	return counter
}

func (d *Display) print() string {
	output := []string{}
	for row := range d.rows {
		for col := range d.cols {
			output = append(output, d.grid[row][col])
		}
		output = append(output, "\n")
	}
	return strings.Join(output, "")
}

func parse(filename string) []Instruction {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	rect_regex := regexp.MustCompile(`rect (\d+)x(\d+)`)
	rotrow_regex := regexp.MustCompile(`rotate row y=(\d+) by (\d+)`)
	rotrcol_regex := regexp.MustCompile(`rotate column x=(\d+) by (\d+)`)

	instructions := []Instruction{}

	for _, line := range lines {
		rect_match := rect_regex.FindStringSubmatch(line)
		rotrow_match := rotrow_regex.FindStringSubmatch(line)
		rotcol_match := rotrcol_regex.FindStringSubmatch(line)

		var instruction_type InstructionType
		var a int
		var b int

		if len(rect_match) > 0 {
			a, _ = strconv.Atoi(rect_match[1])
			b, _ = strconv.Atoi(rect_match[2])
			instruction_type = InstructionType(RECT)
		} else if len(rotrow_match) > 0 {
			a, _ = strconv.Atoi(rotrow_match[1])
			b, _ = strconv.Atoi(rotrow_match[2])
			instruction_type = InstructionType(ROT_ROW)
		} else if len(rotcol_match) > 0 {
			a, _ = strconv.Atoi(rotcol_match[1])
			b, _ = strconv.Atoi(rotcol_match[2])
			instruction_type = InstructionType(ROT_COL)
		}

		instructions = append(instructions, Instruction{instruction_type, a, b})
	}
	return instructions
}

func solve(instructions []Instruction, display *Display) (int, string) {
	for _, instruction := range instructions {
		switch instruction.type_ {
		case InstructionType(RECT):
			display.rect(instruction.a, instruction.b)

		case InstructionType(ROT_ROW):
			display.rot_row(instruction.a, instruction.b)

		case InstructionType(ROT_COL):
			display.rot_col(instruction.a, instruction.b)

		default:
		}
	}
	return display.count(), display.print()
}

func solution(filename string, rows, cols int) (int, string) {
	instructions := parse(filename)
	display := NewDisplay(rows, cols)
	return solve(instructions, display)
}

func main() {
	lit_example, example_display := solution("./example.txt", 3, 7) // 6
	lit_pixels, display := solution("./input.txt", 6, 50)           // 115 and EFEYKFRFIJ

	fmt.Println("Example")
	fmt.Println("-------")
	fmt.Println("display:")
	fmt.Println(example_display)
	fmt.Println("lit pixels:", lit_example)
	fmt.Println()
	fmt.Println("Both parts")
	fmt.Println("----------")
	fmt.Println("display (part 2):")
	fmt.Println(display)
	fmt.Println("lit pixels (part 1):", lit_pixels)
}
