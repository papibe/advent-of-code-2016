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
	raw_name string
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

func (r *Room) decrypt() string {
	plain := []string{}
	for _, char := range r.raw_name {
		var plain_char int
		if char == '-' {
			plain_char = int(' ')
		} else {
			plain_char = (int(char)-'a'+r.sector)%26 + 'a'
		}
		plain = append(plain, string(rune(plain_char)))
	}
	return strings.Join(plain, "")
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
		raw_name := strings.Join(tmp2[:len(tmp2)-1], "-")

		rooms = append(rooms, Room{name, raw_name, sector, checksum})
	}

	return rooms
}

func solve(rooms []Room) int {
	for _, room := range rooms {
		if room.is_real() {
			if room.decrypt() == "northpole object storage" {
				return room.sector
			}
		}
	}
	return -1
}

func solution(filename string) int {
	rooms := parse(filename)
	return solve(rooms)
}

func main() {
	fmt.Println(solution("./input.txt")) // 324
}
