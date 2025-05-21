package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

func md5_hash(text string) string {
	hash := md5.Sum([]byte(text))
	// fmt.Printf("%T\n", hash)
	return hex.EncodeToString(hash[:])
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
			triple_char = previous_char
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

	for keys.len() < 64 {
		s := salt + strconv.Itoa(index)
		hash := md5_hash(s)
		found3, char3, repeated_fives := count_repetitions(hash)

		if found3 {
			_, char3_in_candidates := candidates[char3]
			if !char3_in_candidates {
				candidates[char3] = []int{}
			}
			candidates[char3] = append(candidates[char3], index)

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
		}
		index++
	}
	return -1
}

func main() {
	fmt.Println(solution("abc"))      // 22728
	fmt.Println(solution("cuanljph")) // 23769
}
