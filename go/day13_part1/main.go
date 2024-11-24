package main

import (
	"fmt"
)

type QueueItem struct {
	x     int
	y     int
	steps int
}

type Queue []QueueItem

func (q *Queue) popleft() (int, int, int) {
	item := (*q)[0]
	(*q) = (*q)[1:]
	return item.x, item.y, item.steps
}

func (q *Queue) append(x, y, steps int) {
	(*q) = append((*q), QueueItem{x, y, steps})
}

func (q Queue) isEmpty() bool {
	return len(q) == 0
}

type VisitedItem struct {
	x int
	y int
}

type VisitedSet map[VisitedItem]bool

func (v *VisitedSet) add(x, y int) {
	(*v)[VisitedItem{x, y}] = true
}

func (v *VisitedSet) contains(x, y int) bool {
	_, ok := (*v)[VisitedItem{x, y}]
	return ok
}

func is_open(x, y, favorite_number int) bool {
	value := x*x + 3*x + 2*x*y + y + y*y + favorite_number
	bit_sum := 0
	bit := 1
	for shift := 0; shift < 32; shift++ {
		if (value & (bit << shift)) != 0 {
			bit_sum += 1
		}
	}
	return bit_sum%2 == 0
}

func solution(favorite_number, xgoal, ygoal int) int {
	// BFS setup
	queue := Queue{}
	queue.append(1, 1, 0)
	visited := make(VisitedSet)
	visited.add(1, 1)

	// BFS
	for !queue.isEmpty() {
		x, y, steps := queue.popleft()
		if x == xgoal && y == ygoal {
			return steps
		}

		for _, newcoord := range []VisitedItem{{x + 1, y}, {x - 1, y}, {x, y + 1}, {x, y - 1}} {
			newx, newy := newcoord.x, newcoord.y
			if newx >= 0 &&
				newy >= 0 &&
				is_open(newx, newy, favorite_number) &&
				!visited.contains(newx, newy) {

				queue.append(newx, newy, steps+1)
				visited.add(newx, newy)
			}

		}
	}
	return -1
}

func main() {
	fmt.Println(solution(10, 7, 4))     // 11
	fmt.Println(solution(1362, 31, 39)) // 82
}
