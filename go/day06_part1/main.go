package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

func parse(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func solve(data []string) string {
	frequencies := []map[rune]int{}
	for i := 0; i < len(data[0]); i++ {
		frequencies = append(frequencies, make(map[rune]int))
	}

	for _, word := range data {
		for index, char := range word {
			value, ok := frequencies[index][char]
			if !ok {
				value = 0
			}
			frequencies[index][char] = value + 1
		}
	}

	message := []string{}
	for _, frequency := range frequencies {
		max_freq := math.MinInt
		max_char := ' '

		for char, freq := range frequency {
			if freq > max_freq {
				max_freq = freq
				max_char = char
			}
		}
		message = append(message, string(max_char))
	}
	return strings.Join(message, "")
}

func solution(filename string) string {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example.txt")) // easter
	fmt.Println(solution("./input.txt"))   // umejzgdw
}
