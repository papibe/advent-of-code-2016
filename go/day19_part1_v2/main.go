package main

import (
	"fmt"
	"math"
)

func josephus(n int) int {
	m := math.Floor(math.Log2(float64(n)))
	l := (n - int(math.Pow(2, m)))
	return 2*l + 1
}

func solution(number_of_elves int) int {
	return josephus(number_of_elves)
}

func main() {
	fmt.Println(solution(5))       // 3
	fmt.Println(solution(3014387)) // 1834471
}
