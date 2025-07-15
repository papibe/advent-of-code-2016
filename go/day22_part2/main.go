package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const INVALID = -1

type Coords struct {
	y int
	x int
}

type Node struct {
	x     int
	y     int
	size  int
	used  int
	avail int
}

type Grid struct {
	grid     [][]Node
	Y        int
	X        int
	empty_y  int
	empty_x  int
	g_y      int
	g_x      int
	max_size int
}

type MainQueueItem struct {
	steps   int
	current Coords
	empty   Coords
}

type VisitedItem struct {
	current Coords
	empty   Coords
}

type SecondaryQueueItem struct {
	steps   int
	current Coords
}

func NewGrid(grid [][]Node, empty_y, empty_x, g_y, g_x int) *Grid {
	empty_node := grid[empty_y][empty_x]
	new_grid := Grid{
		grid,
		len(grid),
		len(grid[0]),
		empty_y,
		empty_x,
		g_y,
		g_x,
		empty_node.size,
	}
	return &new_grid
}

func (g *Grid) get_neighbors(y, x int) []Coords {
	neighbors := []Coords{}

	for _, point := range [][]int{{y - 1, x}, {y, x - 1}, {y + 1, x}, {y, x + 1}} {
		new_y, new_x := point[0], point[1]
		if 0 <= new_y && new_y < g.Y && 0 <= new_x && new_x < g.X {
			neighbors = append(neighbors, Coords{new_y, new_x})
		}
	}
	return neighbors
}

func (g *Grid) get_empty() Coords {
	for y, line := range g.grid {
		for x, node := range line {
			if node.used == 0 {
				return Coords{y, x}
			}
		}
	}
	return Coords{-1, -1}
}

func parse(filename string) *Grid {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	nodes := []Node{}
	re_node := regexp.MustCompile(`/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%`)

	max_x := -1
	max_y := -1
	var empty_y int
	var empty_x int

	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for i := 2; i < len(lines); i++ {
		line := lines[i]
		matches := re_node.FindStringSubmatch(line)

		x, _ := strconv.Atoi(matches[1])
		y, _ := strconv.Atoi(matches[2])
		size, _ := strconv.Atoi(matches[3])
		used, _ := strconv.Atoi(matches[4])
		avail, _ := strconv.Atoi(matches[5])

		nodes = append(nodes, Node{x, y, size, used, avail})

		max_x = max(max_x, x)
		max_y = max(max_y, y)
		if used == 0 {
			empty_y = y
			empty_x = x
		}
	}
	grid := make([][]Node, max_y+1)
	for i := range max_y + 1 {
		grid[i] = make([]Node, max_x+1)
	}

	for _, node := range nodes {
		grid[node.y][node.x] = node
	}

	return NewGrid(grid, empty_y, empty_x, 0, max_x)
}

func move_empty_to_neighbor(
	grid *Grid,
	current_y,
	current_x,
	destination_y,
	destination_x,
	g_y,
	g_x int,
) int {
	// BFS init
	queue := NewQueue[SecondaryQueueItem]()
	queue.append(SecondaryQueueItem{0, Coords{current_y, current_x}})

	visited := NewSet[Coords]()
	visited.add(Coords{current_y, current_x})

	// BFS
	for !queue.is_empty() {
		item := queue.popleft()
		steps, current := item.steps, item.current

		if current.y == destination_y && current.x == destination_x {
			return steps
		}
		for _, neighbor := range grid.get_neighbors(current.y, current.x) {
			// skip full nodes (#)
			if grid.grid[neighbor.y][neighbor.x].used > grid.max_size {
				continue
			}
			// don't pass over G
			if neighbor.y == g_y && neighbor.x == g_x {
				continue
			}
			if visited.contains(neighbor) {
				continue
			}
			queue.append(SecondaryQueueItem{steps + 1, neighbor})
			visited.add(neighbor)
		}
	}
	return INVALID
}

func solve(
	grid *Grid,
	current_y,
	current_x,
	empty_y,
	empty_x,
	destination_y,
	destination_x int,
) int {
	// BFS init
	current := Coords{current_y, current_x}
	empty := Coords{empty_y, empty_x}

	queue := NewQueue[MainQueueItem]()
	queue.append(MainQueueItem{0, current, empty})

	visited := NewSet[VisitedItem]()
	visited.add(VisitedItem{current, empty})

	for !queue.is_empty() {
		item := queue.popleft()
		steps, current, empty := item.steps, item.current, item.empty

		if current.y == destination_y && current.x == destination_x {
			return steps
		}

		for _, neighbor := range grid.get_neighbors(current.y, current.x) {
			// skip full nodes (#)
			if grid.grid[neighbor.y][neighbor.x].used > grid.max_size {
				continue
			}
			if visited.contains(VisitedItem{neighbor, current}) {
				continue
			}
			// move empty space to neighbor
			intermediate_steps := move_empty_to_neighbor(
				grid,
				empty.y,
				empty.x,
				neighbor.y,
				neighbor.x,
				current.y,
				current.x,
			)
			if intermediate_steps == INVALID {
				panic("say what!?")
			}
			queue.append(MainQueueItem{steps + intermediate_steps + 1, neighbor, current})
			visited.add(VisitedItem{neighbor, current})
		}
	}
	return INVALID
}

func solution(filename string) int {
	grid := parse(filename)
	// for _, row := range grid.grid {
	// 	for _, item := range row {
	// 		fmt.Println(item)
	// 	}
	// }

	return solve(
		grid,
		grid.g_y,
		grid.g_x,
		grid.empty_y,
		grid.empty_x,
		0,
		0,
	)
}

func main() {
	fmt.Println(solution("./example.txt")) // 7
	fmt.Println(solution("./input.txt"))   // 215
}
