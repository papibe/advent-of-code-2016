package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"math"
	"strings"
)

var MAZE = []string{
	"#########",
	"#S| | | #",
	"#-#-#-#-#",
	"# | | | #",
	"#-#-#-#-#",
	"# | | | #",
	"#-#-#-#-#",
	"# | | |V#",
	"#########",
}

const START = 'S'
const WALL = '#'
const SPACE = ' '
const VAULT = 'V'

var DOORS = []string{"U", "D", "L", "R"}

var STEPS = map[string][]int{
	"U": {-1, 0},
	"D": {1, 0},
	"L": {0, -1},
	"R": {0, 1},
}

const OPEN_DOOR_CODE = "bcdef"

func md5_hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func is_open_door_code(code rune) bool {
	return code == 'b' || code == 'c' || code == 'd' || code == 'e' || code == 'f'
}

func copy_list(l []string) []string {
	output := []string{}
	output = append(output, l...)
	return output
}

func solve(passcode string, row, col int, path []string, solutions *[][]string) {
	if MAZE[row][col] == VAULT {
		*solutions = append(*solutions, copy_list(path))
		return
	}

	// SPACE or START
	hashed := md5_hash(passcode + strings.Join(path, ""))
	for index := range len(DOORS) {
		d := DOORS[index]
		code := hashed[index]

		if is_open_door_code(rune(code)) {
			row_step, col_step := STEPS[d][0], STEPS[d][1]

			neighbor_row := row + row_step
			neighbor_col := col + col_step

			if MAZE[neighbor_row][neighbor_col] != WALL {
				path = append(path, d)
				solve(passcode, row+2*row_step, col+2*col_step, path, solutions)
				path = path[:len(path)-1]
			}
		}
	}
}

func solution(passcode string) int {
	path := []string{}
	solutions := [][]string{}

	solve(passcode, 1, 1, path, &solutions)

	longest_len := math.MinInt

	for _, p := range solutions {
		longest_len = max(longest_len, len(p))
	}

	return longest_len
}

func main() {
	fmt.Println(solution("yjjvjgan")) // 498
}
