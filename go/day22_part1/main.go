package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Node struct {
	name  string
	used  int
	avail int
}

func parse(filename string) []Node {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	nodes := []Node{}
	re_node := regexp.MustCompile(`/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%`)

	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	for i := 2; i < len(lines); i++ {
		line := lines[i]
		matches := re_node.FindStringSubmatch(line)

		x := matches[1]
		y := matches[2]
		used, _ := strconv.Atoi(matches[4])
		avail, _ := strconv.Atoi(matches[5])
		nodes = append(nodes, Node{fmt.Sprintf("%s,%s", x, y), used, avail})
	}

	return nodes
}

func are_viable(a, b Node) bool {
	if a.used == 0 {
		return false
	}
	if a == b {
		return false
	}
	if a.used <= b.avail {
		return true
	}
	return false
}

func solve(nodes []Node) int {
	viable_pairs_count := 0
	n := len(nodes)

	for i := range n {
		for j := i + 1; j < n; j++ {
			node1 := nodes[i]
			node2 := nodes[j]

			if are_viable(node1, node2) || are_viable(node2, node1) {
				viable_pairs_count++
			}
		}
	}
	return viable_pairs_count
}

func solution(filename string) int {
	nodes := parse(filename)
	return solve(nodes)
}

func main() {
	fmt.Println(solution("./input.txt")) // 903
}
