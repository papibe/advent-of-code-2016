package main

import (
	"fmt"
	"os"
	"strings"
)

const SAFE = '.'
const TRAP = '^'

func parse(filename string) string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Trim(string(data), "\n")
}

func count_safes(tiles string) int {
	safe_titles := 0
	for _, tile := range tiles {
		if tile == SAFE {
			safe_titles++
		}
	}
	return safe_titles
}

func solve(tiles string, times int) int {
	n := len(tiles)

	safe_titles := count_safes(tiles)

	for range times - 1 {
		next_tiles := make([]rune, n)
		for i := 0; i < n; i++ {
			next_tiles[i] = SAFE
		}

		for index := range n {
			next_tile := SAFE

			var left rune
			if index >= 1 {
				left = rune(tiles[index-1])
			} else {
				left = SAFE
			}

			center := tiles[index]

			var right rune
			if index < n-1 {
				right = rune(tiles[index+1])
			} else {
				right = SAFE
			}

			rule1 := (left == TRAP && center == TRAP && right == SAFE)
			rule2 := (center == TRAP && right == TRAP && left == SAFE)
			rule3 := (left == TRAP && center == SAFE && right == SAFE)
			rule4 := (right == TRAP && left == SAFE && center == SAFE)

			if rule1 || rule2 || rule3 || rule4 {
				next_tile = TRAP
			}

			next_tiles[index] = next_tile
		}
		tiles = string(next_tiles)
		safe_titles += count_safes(tiles)

	}

	return safe_titles
}

func solution(filename string, times int) int {
	tiles := parse(filename)
	return solve(tiles, times)
}

func main() {
	fmt.Println(solution("./input.txt", 40)) // 2013
}
