package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

func stretch_hash(text string, times int) string {
	for range times + 1 {
		hash_object := md5.Sum([]byte(text))
		text = hex.EncodeToString(hash_object[:])
	}
	return text
}

func count_repetitions(s string) (bool, string, []string) {
	repeated := 1
	previous_char := ""
	triple_char := ""
	found3 := false

	repeated_fives := []string{}

	for _, char := range s {
		if string(char) == previous_char {
			repeated++
		} else {
			repeated = 1
		}

		if repeated == 3 && triple_char == "" {
			triple_char = string(char)
			found3 = true
		}

		if repeated == 5 {
			repeated_fives = append(repeated_fives, string(char))
		}

		previous_char = string(char)
	}

	return found3, triple_char, repeated_fives
}

func solution(salt string) int {
	index := 0
	keys := NewSet[int]()

	candidates := make(map[string][]int)

	for {
		s := salt + strconv.Itoa(index)
		hash := stretch_hash(s, 2016)
		found3, char3, repeated_fives := count_repetitions(hash)

		if found3 {
			_, char3_in_candidates := candidates[char3]
			if !char3_in_candidates {
				candidates[char3] = []int{}
			}
			candidates[char3] = append(candidates[char3], index)
		}

		for _, char := range repeated_fives {
			_, char_in_candidates := candidates[char]
			if char_in_candidates {
				for _, previous_index := range candidates[char] {
					if index > previous_index && index-previous_index <= 1000 {
						keys.add(previous_index)
						if keys.len() == 64 {
							return previous_index
						}
					}
				}
			}
		}
		index++
	}
	return -1
}

func main() {
	fmt.Println(solution("cuanljph")) // 20606
}
