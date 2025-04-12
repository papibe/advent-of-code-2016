package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

func parse(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func got_abba(word string) bool {
	n := len(word)

	if n < 4 {
		return false
	}
	for index := range n - 4 + 1 {
		if word[index] == word[index+3] &&
			word[index+1] == word[index+2] &&
			word[index] != word[index+1] {
			return true
		}
	}
	return false
}

func parse_ip(ip string) ([]string, []string) {
	outers := []string{}
	hypernets := []string{}

	outer_regex := regexp.MustCompile(`^\w+`)
	hypernet_regex := regexp.MustCompile(`^\[(\w+)\]`)

	for len(ip) > 0 {
		outer_matches := outer_regex.FindStringSubmatch(ip)
		hypernet_matches := hypernet_regex.FindStringSubmatch(ip)

		if len(outer_matches) > 0 {
			a_match := outer_matches[0]
			outers = append(outers, a_match)
			ip = ip[len(a_match):]

		} else if len(hypernet_matches) > 0 {
			a_match := hypernet_matches[1]
			hypernets = append(hypernets, a_match)
			ip = ip[len(a_match)+2:]
		}
	}
	return outers, hypernets
}

func supports_tls(ip string) bool {
	outers, hypernets := parse_ip(ip)

	abba_in_outer := false
	for _, outer := range outers {
		abba_in_outer = abba_in_outer || got_abba(outer)
	}

	abba_in_hypernet := false
	for _, hypernet := range hypernets {
		abba_in_hypernet = abba_in_hypernet || got_abba(hypernet)
	}

	if abba_in_outer && !abba_in_hypernet {
		return true
	}
	return false
}

func solve(data []string) int {
	supported := 0

	for _, ip := range data {
		if supports_tls(ip) {
			supported++
		}
	}
	return supported
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./input.txt")) // 110
}
