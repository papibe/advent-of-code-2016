package main

import (
	"fmt"
)

func josephus_180(n int) int {
	if n == 1 || n == 2 {
		return 1
	}

	if n == 3 {
		return 3
	}

	mod := n % 3
	if mod == 0 {
		return 3 * josephus_180(n/3)
	}

	length := (n + 2) / 3
	sub_problem := josephus_180(length)
	half := length / 2

	if sub_problem <= half {
		return (3 * sub_problem) - (3 - mod)
	} else {
		return (3 * sub_problem) - 2*(3-mod)
	}

}

func solution(number_of_elves int) int {
	return josephus_180(number_of_elves)
}

func main() {
	fmt.Println(solution(5))       // 2
	fmt.Println(solution(3014387)) // 1420064
}
