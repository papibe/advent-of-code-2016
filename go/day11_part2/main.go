package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

type QueueItem struct {
	steps    int
	building *Building
}

func parse(filename string) *Building {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	microchip_regex := regexp.MustCompile(`(\w+)-\w+ microchip`)
	gen_regex := regexp.MustCompile(`(\w+) generator`)

	floors := []*Floor{}

	for _, line := range lines {
		microchip_matches := microchip_regex.FindAllStringSubmatch(line, -1)
		gen_matches := gen_regex.FindAllStringSubmatch(line, -1)

		microchips := NewSet[Material]()
		generators := NewSet[Material]()

		for _, microchip := range microchip_matches {
			microchips.add(*NewMicrochip(microchip[1]))
		}

		for _, generator := range gen_matches {
			generators.add(*NewGenerator(generator[1]))
		}

		floors = append(floors, NewFloor(microchips, generators))
	}

	return &Building{0, floors, len(floors)}
}

func solve(building *Building) int {
	// BFS setup
	queue := NewQueue[QueueItem]()
	queue.append(QueueItem{0, building})
	visited := NewSet[string]()
	state_key := building.hash()
	visited.add(state_key)

	// BFS
	for queue.len() > 0 {
		state := queue.popleft()
		steps, building := state.steps, state.building

		if building.all_on_4th() {
			return steps
		}

		for _, next_building := range building.next_states() {
			state_key := next_building.hash()
			if !visited.contains(state_key) && next_building.is_radiation_ok() {
				queue.append(QueueItem{steps + 1, next_building})
				visited.add(state_key)
			}
		}
	}

	return -1
}

func solution(filename string, value1, value2 int) int {
	building := parse(filename)

	// Patch building for part 2
	building.floors[0].push(*NewGenerator("elerium"))
	building.floors[0].push(*NewMicrochip("elerium"))
	building.floors[0].push(*NewGenerator("dilithium"))
	building.floors[0].push(*NewMicrochip("dilithium"))

	return solve(building)
}

func main() {
	fmt.Println(solution("./input.txt", 17, 61)) // 61
}
