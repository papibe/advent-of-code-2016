package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strings"
)

type HeapItem struct {
	row  int
	col  int
	path []string
}

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
	// BFS init
	heap := NewPriorityQueue[HeapItem]()
	heap.Push(HeapItem{1, 1, []string{}}, 0)

	// BFS
	for !heap.IsEmpty() {
		item, steps := heap.Pop()
		row, col, path := item.row, item.col, item.path

		if MAZE[row][col] == VAULT {
			return strings.Join(path, "")
		}

		hashed := md5_hash(passcode + strings.Join(path, ""))
		for index := range len(DOORS) {
			d := DOORS[index]
			code := hashed[index]

			if is_open_door_code(rune(code)) {
				row_step, col_step := STEPS[d][0], STEPS[d][1]

				neighbor_row := row + row_step
				neighbor_col := col + col_step

				if MAZE[neighbor_row][neighbor_col] != WALL {
					new_path := copy_list(path)
					new_path = append(new_path, d)
					heap.Push(HeapItem{row + 2*row_step, col + 2*col_step, new_path}, steps+1)
				}
			}
		}

	}
	return ""
}

func main() {
	fmt.Println(solution("yjjvjgan")) // RLDRUDRDDR
}
