package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(filename string) string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Trim(string(data), "\n")
}

func uncompress(sequence []byte) int {
	marker_regex := regexp.MustCompile(`\((\d+)x(\d+)\)`)
	output_len := 0

	for {
		matches := marker_regex.FindSubmatchIndex(sequence)

		var start_index, end_index, amount, times int

		if matches != nil {
			start_index = matches[0]
			end_index = matches[1]
			amount, _ = strconv.Atoi(string(sequence[matches[2]:matches[3]]))
			times, _ = strconv.Atoi(string(sequence[matches[4]:matches[5]]))
		} else {
			output_len += len(sequence)
			break
		}

		// add prefix with no marker
		output_len += start_index

		// calculate indexes for uncompress nested sequence
		next_start_index := end_index
		next_end_index := end_index + amount

		output_len += times * uncompress(sequence[next_start_index:next_end_index])

		sequence = sequence[next_end_index:]
	}
	return output_len
}

func solution(filename string) int {
	sequence := parse(filename)
	return uncompress([]byte(sequence))
}

func main() {
	fmt.Println(solution("./input.txt")) // 10774309173
}
