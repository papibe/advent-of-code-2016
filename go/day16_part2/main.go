package main

import (
	"fmt"
)

var INVERT = map[rune]rune{
	'0': '1',
	'1': '0',
}

func reversed_invert(s *[]rune) []rune {
	n := len(*s)
	result := make([]rune, n)

	for i := range n {
		result[n-1-i] = INVERT[(*s)[i]]
	}
	return result
}

func check_sum(data []rune) string {
	var checksum []rune

	for {
		checksum = make([]rune, len(data)/2)
		checksum_index := 0

		for index := 0; index < len(data); index += 2 {
			if data[index] == data[index+1] {
				checksum[checksum_index] = '1'
			} else {
				checksum[checksum_index] = '0'
			}
			checksum_index++
		}
		if len(checksum)%2 != 0 {
			break
		}
		data = checksum
	}
	return string(checksum)
}

func solution(puzzle_input string, length int) string {
	a := []rune(puzzle_input)

	for len(a) < length {
		a = append(a, '0')
		a_reversed_inverted := reversed_invert(&a)
		a = append(a, a_reversed_inverted...)

	}
	return check_sum(a[:length])
}

func main() {
	fmt.Println(solution("10001110011110000", 35651584)) // 01100111101101111
}
