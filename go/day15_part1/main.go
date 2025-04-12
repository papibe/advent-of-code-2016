package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Disc struct {
	id          int
	slots       int
	time        int
	initial_pos int
}

func parse(filename string) []Disc {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	discs := []Disc{}
	regex := regexp.MustCompile(`Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)`)

	for _, line := range lines {
		matches := regex.FindStringSubmatch(line)

		disc_id, _ := strconv.Atoi(matches[1])
		slots, _ := strconv.Atoi(matches[2])
		time, _ := strconv.Atoi(matches[3])
		initial_position, _ := strconv.Atoi(matches[4])

		discs = append(discs, Disc{disc_id, slots, time, initial_position})
	}

	return discs
}

func solve(discs []Disc) int {
	timestamp := 0

	for {
		position_ok := true

		for index := range len(discs) {
			disc := discs[index]
			time_shift := index + 1

			position := (disc.initial_pos + timestamp + time_shift) % disc.slots

			if position != 0 {
				position_ok = false
				break
			}
		}
		if position_ok {
			return timestamp
		}
		timestamp++
	}

}

func solution(filename string) int {
	discs := parse(filename)
	return solve(discs)
}

func main() {
	fmt.Println(solution("./example.txt")) // 5
	fmt.Println(solution("./input.txt"))   // 203660
}
