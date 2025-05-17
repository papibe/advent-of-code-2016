package main

import (
	"testing"
)

const WALL = '#'
const SPACE = '.'

var layout = []string{
	".#.####.##",
	"..#..#...#",
	"#....##...",
	"###.#.###.",
	".##..#..#.",
	"..##....#.",
	"#...##.###",
}

func TestIsOpen(t *testing.T) {
	for y, row := range layout {
		for x, cube := range row {
			var result rune
			if is_open(x, y, 10) {
				result = SPACE
			} else {
				result = WALL
			}
			if result != cube {
				t.Errorf("at (%d, %d): got %c; want %c", x, y, result, cube)
			}
		}
	}

}
