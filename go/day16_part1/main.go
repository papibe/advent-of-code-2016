package main

import (
	"fmt"
	"strings"
)

func reversed(s []string) []string {
	n := len(s)
	result := make([]string, n)

	for i := range n {
		result[n-1-i] = s[i]
	}
	return result
}

func check_sum(data []string) string {
	var checksum []string

	for {
		checksum = []string{}

		for index := 0; index < len(data); index += 2 {
			if data[index] == data[index+1] {
				checksum = append(checksum, "1")
			} else {
				checksum = append(checksum, "0")
			}
		}
		if len(checksum)%2 != 0 {
			break
		} else {
			data = checksum
		}
	}
	return strings.Join(checksum, "")
}

func solution(puzzle_input string, length int) string {
	a := strings.Split(puzzle_input, "")

	for len(a) < length {
		a_reversed := reversed(a)
		a = append(a, "0")

		for _, char := range a_reversed {
			if char == "1" {
				a = append(a, "0")
			} else {
				a = append(a, "1")
			}
		}
	}
	return check_sum(a[:length])
}

func main() {
	fmt.Println(solution("10000", 20))              // 01100
	fmt.Println(solution("10001110011110000", 272)) // 10010101010011101
}
