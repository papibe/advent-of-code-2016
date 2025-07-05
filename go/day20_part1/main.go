package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Range struct {
	low  int
	high int
}

func parse(filename string) []Range {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	ranges := []Range{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	for _, line := range lines {
		split_line := strings.Split(line, "-")

		low, _ := strconv.Atoi(split_line[0])
		high, _ := strconv.Atoi(split_line[1])

		ranges = append(ranges, Range{low, high})
	}
	return ranges
}

func solve(ranges []Range) int {
	min_ip := 0

	sort.Slice(ranges, func(i, j int) bool {
		if ranges[i].low != ranges[j].low {
			return ranges[i].low < ranges[j].low
		}

		return ranges[i].high < ranges[j].high
	})

	for _, r := range ranges {
		if r.low <= min_ip && min_ip <= r.high {
			min_ip = r.high + 1
		}
	}
	return min_ip
}

func solution(filename string) int {
	ranges := parse(filename)
	return solve(ranges)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3
	fmt.Println(solution("./input.txt"))   // 23923783
}
