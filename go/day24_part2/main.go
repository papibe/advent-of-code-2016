package main

import (
	"fmt"
	"math"
	"os"
	"strings"
	"unicode"
)

const WALL = '#'

type Position struct {
	row int
	col int
}

func (p Position) hash() int {
	return p.row*27 + p.col*31
}

type Node int

type AdjacencyMatrix [][]int

type Positions map[Node]Position

type QueueItem struct {
	steps    int
	position Position
}

func get_shortest_distance(
	grid []string,
	am AdjacencyMatrix,
	node_positions Positions,
	node Node,
	other_node Node,
) int {
	// BFS setup
	queue := NewQueue[QueueItem]()
	queue.append(QueueItem{0, node_positions[node]})

	visited := NewSet[Position]()
	visited.add(node_positions[node])

	// BFS
	for !queue.is_empty() {
		item := queue.popleft()
		steps, pos := item.steps, item.position

		if pos == node_positions[other_node] {
			return steps
		}

		for _, new_pos := range []Position{
			{pos.row + 1, pos.col},
			{pos.row - 1, pos.col},
			{pos.row, pos.col + 1},
			{pos.row, pos.col - 1},
		} {
			new_row, new_col := new_pos.row, new_pos.col

			if 0 <= new_row && new_row < len(grid) && 0 <= new_col && new_col < len(grid[0]) {
				if grid[new_row][new_col] == WALL {
					continue
				}

				if !visited.contains(new_pos) {
					queue.append(QueueItem{steps + 1, new_pos})
					visited.add(new_pos)
				}
			}
		}

	}

	return -1
}

func parse(filename string) (AdjacencyMatrix, Positions) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}
	grid := strings.Split((strings.Trim(string(data), "\n")), "\n")

	// first pass get nodes
	node_positions := make(Positions)
	for row, line := range grid {
		for col, cell := range line {
			if unicode.IsDigit(cell) {
				value := Node(int(cell - '0'))
				node_positions[value] = Position{row, col}
			}
		}
	}

	n := len(node_positions)

	// create adjacency Matrix
	am := make(AdjacencyMatrix, n)
	for i := range n {
		am[i] = make([]int, n)
		for j := range n {
			am[i][j] = math.MaxInt
		}
	}

	// calculate mutual distances
	for node := range n {
		am[node][node] = 0
	}

	for node := range n {
		for other_node := node + 1; other_node < n; other_node++ {
			distance := get_shortest_distance(grid, am, node_positions, Node(node), Node(other_node))
			am[node][other_node] = distance
			am[other_node][node] = distance
		}
	}

	return am, node_positions
}

func solve(am AdjacencyMatrix, start_node Node, number_of_nodes int) int {
	min_distance := math.MaxInt
	visited := make([]bool, number_of_nodes)
	for i := range number_of_nodes {
		visited[i] = false
	}

	var dfs func(node Node, steps int)

	dfs = func(node Node, steps int) {
		all_visited := true
		for i := range number_of_nodes {
			if !visited[i] {
				all_visited = false
				break
			}
		}

		if all_visited {
			min_distance = min(min_distance, steps+am[node][0])
			return
		}

		visited[node] = true

		for other_node := range number_of_nodes {
			if !visited[other_node] {
				visited[other_node] = true
				dfs(Node(other_node), steps+am[node][other_node])
				visited[other_node] = false
			}
		}
	}

	dfs(0, 0)
	return min_distance
}

func solution(filename string) int {
	adjacency_matrix, node_positions := parse(filename)
	return solve(adjacency_matrix, 0, len(node_positions))
}

func main() {
	fmt.Println(solution("./input.txt")) // 652
}
