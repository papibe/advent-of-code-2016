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

const WALL = '#'
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

func solution(passcode string) string {

	shortest_len := math.MaxInt
	var shortest_path []string
	var dfs func(row, col int, path *[]string)

	dfs = func(row, col int, path *[]string) {

		if MAZE[row][col] == VAULT {
			if len(*path) < shortest_len {
				shortest_len = len(*path)
				shortest_path = copy_list(*path)
			}
			return
		}

		if len(*path) > shortest_len {
			return
		}

		// SPACE or START
		hashed := md5_hash(passcode + strings.Join(*path, ""))
		for index := range len(DOORS) {
			d := DOORS[index]
			code := hashed[index]

			if is_open_door_code(rune(code)) {
				row_step, col_step := STEPS[d][0], STEPS[d][1]

				neighbor_row := row + row_step
				neighbor_col := col + col_step

				if MAZE[neighbor_row][neighbor_col] != WALL {
					*path = append(*path, d)
					dfs(row+2*row_step, col+2*col_step, path)
					*path = (*path)[:len(*path)-1]
				}
			}
		}
	}

	dfs(1, 1, &[]string{})
	return strings.Join(shortest_path, "")
}

func main() {
	fmt.Println(solution("yjjvjgan")) // RLDRUDRDDR
}
