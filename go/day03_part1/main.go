package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Triangle struct {
	side1 int
	side2 int
	side3 int
}

func check_side(s1, s2, s3 int) bool {
	return s1+s2 > s3
}

func (t Triangle) check() bool {
	side1_is_ok := check_side(t.side2, t.side3, t.side1)
	side2_is_ok := check_side(t.side1, t.side3, t.side2)
	side3_is_ok := check_side(t.side1, t.side2, t.side3)

	return side1_is_ok && side2_is_ok && side3_is_ok
}

func parse(filename string) []Triangle {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	triangles := []Triangle{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	regex := regexp.MustCompile(`\s+`)

	for _, line := range lines {
		sides := regex.Split(strings.Trim(line, " "), -1)
		side1, _ := strconv.Atoi(sides[0])
		side2, _ := strconv.Atoi(sides[1])
		side3, _ := strconv.Atoi(sides[2])

		triangles = append(triangles, Triangle{side1, side2, side3})
	}

	return triangles
}

func solve(triangles []Triangle) int {
	possibles := 0

	for _, triangle := range triangles {
		if triangle.check() {
			possibles++
		}
	}
	return possibles
}

func solution(filename string) int {
	triangles := parse(filename)
	return solve(triangles)
}

func main() {
	fmt.Println(solution("./input.txt")) // 1050
}
