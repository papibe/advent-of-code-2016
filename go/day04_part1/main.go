package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Room struct {
	name     string
	sector   int
	checksum string
}

func (r *Room) is_real() bool {
	// get frequency
	frequency := make(map[string]int)
	for _, char := range r.name {
		schar := string(char)
		value, ok := frequency[schar]
		if !ok {
			frequency[schar] = value
		}
		frequency[schar] += 1
	}

	// bucket sort
	bucket := make(map[int][]string)
	for k, v := range frequency {
		_, ok := bucket[v]
		if !ok {
			bucket[v] = []string{}
		}
		bucket[v] = append(bucket[v], string(k))
	}

	// sort alphabetically
	for _, v := range bucket {
		sort.Slice(v, func(i, j int) bool {
			return v[i] < v[j]
		})
	}

	// sort frequencies
	sorted_freqs := []int{}
	for k, _ := range bucket {
		sorted_freqs = append(sorted_freqs, k)
	}
	sort.Slice(sorted_freqs, func(i, j int) bool {
		return sorted_freqs[i] > sorted_freqs[j]
	})

	// calculate checksum
	checksum := []string{}
	for _, freq := range sorted_freqs {
		checksum = append(checksum, bucket[freq]...)
	}

	return strings.Join(checksum, "")[:5] == r.checksum
}

func parse(filename string) []Room {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	rooms := []Room{}

	for _, line := range lines {
		tmp := strings.Split(line, "[")
		tmp_checksum := (tmp[len(tmp)-1])
		checksum := tmp_checksum[:len(tmp_checksum)-1]

		tmp2 := strings.Split(tmp[0], "-")
		sector, _ := strconv.Atoi(tmp2[len(tmp2)-1])
		name := strings.Join(tmp2[:len(tmp2)-1], "")

		rooms = append(rooms, Room{name, sector, checksum})
	}

	return rooms
}

func solve(rooms []Room) int {
	sector_sum := 0

	for _, room := range rooms {
		if room.is_real() {
			sector_sum += room.sector
		}
	}
	return sector_sum
}

func solution(filename string) int {
	rooms := parse(filename)
	return solve(rooms)
}

func main() {
	fmt.Println(solution("./example.txt")) // 1514
	fmt.Println(solution("./input.txt"))   // 245102
}
