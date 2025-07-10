package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func mod(a, b int) int {
	// equivalent function to % in python
	return (a%b + b) % b
}

func map_copy[T comparable, R any](original map[T]R) map[T]R {
	copied := make(map[T]R, len(original))

	for key, value := range original {
		copied[key] = value
	}
	return copied
}

func maps_are_equal(s1, s2 map[rune]int) bool {

	if len(s1) != len(s2) {
		return false
	}
	for k, v1 := range s1 {
		v2, ok := s2[k]
		if !ok {
			return false
		}
		if v1 != v2 {
			return false
		}
	}
	return true
}

func solve(data []string, password string) string {
	p := []rune(password)

	letter_mapping := make(map[rune]int)
	index_mapping := make(map[int]rune)

	for index, char := range p {
		letter_mapping[char] = index
		index_mapping[index] = char
	}

	re_swap_pos := regexp.MustCompile(`swap position (\d) with position (\d)`)
	re_swap_letter := regexp.MustCompile(`swap letter (\w) with letter (\w)`)
	re_rotate_lr := regexp.MustCompile(`rotate (left|right) (\d) step`)
	re_rotate_position := regexp.MustCompile(`rotate based on position of letter (\w)`)
	re_reverse := regexp.MustCompile(`reverse positions (\d) through (\d)`)
	re_move := regexp.MustCompile(`move position (\d) to position (\d)`)

	// Reverse the data slice in-place
	for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
		data[i], data[j] = data[j], data[i]
	}

	for _, line := range data {
		matches := re_swap_pos.FindStringSubmatch(line)
		if len(matches) > 0 {
			index1, _ := strconv.Atoi(matches[1])
			index2, _ := strconv.Atoi(matches[2])

			letter1 := index_mapping[index1]
			letter2 := index_mapping[index2]

			letter_mapping[letter1] = index2
			letter_mapping[letter2] = index1

			index_mapping[index1] = letter2
			index_mapping[index2] = letter1
			continue
		}

		matches = re_swap_letter.FindStringSubmatch(line)
		if len(matches) > 0 {
			letter1 := []rune(matches[1])[0]
			letter2 := []rune(matches[2])[0]

			index1 := letter_mapping[letter1]
			index2 := letter_mapping[letter2]

			letter_mapping[letter1] = index2
			letter_mapping[letter2] = index1

			index_mapping[index1] = letter2
			index_mapping[index2] = letter1
			continue
		}

		matches = re_rotate_lr.FindStringSubmatch(line)
		if len(matches) > 0 {
			direction := matches[1]
			steps, _ := strconv.Atoi(matches[2])

			var incr int

			if direction == "left" {
				incr = 1
			} else {
				incr = -1
			}

			for letter, _ := range letter_mapping {
				new_index := mod(letter_mapping[letter]+(incr*steps), len(letter_mapping))
				letter_mapping[letter] = new_index
				index_mapping[new_index] = letter
			}
			continue
		}

		matches = re_rotate_position.FindStringSubmatch(line)
		if len(matches) > 0 {
			rotate_at_letter := []rune(matches[1])[0]

			for steps := 1; steps <= len(letter_mapping); steps++ {
				new_letter_mapping := map_copy(letter_mapping)
				new_index_mapping := map_copy(index_mapping)

				for letter, _ := range letter_mapping {
					new_index := mod(letter_mapping[letter]-steps, len(letter_mapping))
					new_letter_mapping[letter] = new_index
					new_index_mapping[new_index] = letter
				}

				index := new_letter_mapping[rotate_at_letter]

				var rotation_steps int
				if index >= 4 {
					rotation_steps = 1 + index + 1
				} else {
					rotation_steps = 1 + index
				}

				rotation_letter_mapping := map_copy(new_letter_mapping)
				rotation_index_mapping := map_copy(new_index_mapping)

				for letter, _ := range new_letter_mapping {
					new_index := mod(new_letter_mapping[letter]+rotation_steps, len(new_letter_mapping))
					rotation_letter_mapping[letter] = new_index
					rotation_index_mapping[new_index] = letter
				}

				if maps_are_equal(rotation_letter_mapping, letter_mapping) {
					letter_mapping = map_copy(new_letter_mapping)
					index_mapping = map_copy(new_index_mapping)
					break
				}

			}
			continue
		}

		matches = re_reverse.FindStringSubmatch(line)
		if len(matches) > 0 {
			start, _ := strconv.Atoi(matches[1])
			end, _ := strconv.Atoi(matches[2])

			length := end - start + 1
			for i := range length / 2 {
				letter1 := index_mapping[start+i]
				letter2 := index_mapping[end-i]

				index1 := letter_mapping[letter1]
				index2 := letter_mapping[letter2]

				letter_mapping[letter1] = index2
				letter_mapping[letter2] = index1

				index_mapping[index1] = letter2
				index_mapping[index2] = letter1
			}
			continue
		}

		matches = re_move.FindStringSubmatch(line)
		if len(matches) > 0 {
			index2, _ := strconv.Atoi(matches[1])
			index1, _ := strconv.Atoi(matches[2])

			letter_to_move := index_mapping[index1]

			new_letter_mapping := map_copy(letter_mapping)
			new_index_mapping := map_copy(index_mapping)

			if index2 >= index1 {

				for i := index1 + 1; i < index2+1; i++ {
					letter := index_mapping[i]
					new_index := letter_mapping[letter] - 1
					new_letter_mapping[letter] = new_index
					new_index_mapping[new_index] = letter
				}

				new_letter_mapping[letter_to_move] = index2
				new_index_mapping[index2] = letter_to_move

				letter_mapping = new_letter_mapping
				index_mapping = new_index_mapping

			} else {

				for i := index2; i < index1; i++ {
					letter := index_mapping[i]
					new_index := letter_mapping[letter] + 1
					new_letter_mapping[letter] = new_index
					new_index_mapping[new_index] = letter
				}

				new_letter_mapping[letter_to_move] = index2
				new_index_mapping[index2] = letter_to_move

				letter_mapping = new_letter_mapping
				index_mapping = new_index_mapping
			}
			continue
		}
	}

	output := []rune{}
	for i := range len(letter_mapping) {
		output = append(output, index_mapping[i])
	}

	return string(output)
}

func solution(filename string, password string) string {
	functions := parse(filename)
	return solve(functions, password)
}

func main() {
	fmt.Println(solution("./input.txt", "fbgdceah")) // "egcdahbf"
}
