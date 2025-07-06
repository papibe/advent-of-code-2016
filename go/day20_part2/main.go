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

func solve(ranges []Range, max_ip int) int {
	sort.Slice(ranges, func(i, j int) bool {
		if ranges[i].low != ranges[j].low {
			return ranges[i].low < ranges[j].low
		}

		return ranges[i].high < ranges[j].high
	})

	joined_ranges := []Range{ranges[0]}

	for _, incoming := range ranges[1:] {
		last := joined_ranges[len(joined_ranges)-1]
		joined_ranges = joined_ranges[:len(joined_ranges)-1]

		if incoming.low <= last.high+1 {
			joined_ranges = append(joined_ranges, Range{last.low, max(last.high, incoming.high)})
		} else {
			joined_ranges = append(joined_ranges, last)
			joined_ranges = append(joined_ranges, incoming)
		}
	}

	allowed_ips := 0
	last_value := 0

	for _, range_ := range joined_ranges {
		if range_.low > last_value {
			allowed_ips += range_.low - last_value - 1
		}
		last_value = range_.high
	}

	if last_value < max_ip {
		allowed_ips += max_ip - last_value
	}

	return allowed_ips
}

func solution(filename string, max_ip int) int {
	ranges := parse(filename)
	return solve(ranges, max_ip)
}

func main() {
	fmt.Println(solution("./example.txt", 9))        // 2
	fmt.Println(solution("./input.txt", 4294967295)) // 125
}
