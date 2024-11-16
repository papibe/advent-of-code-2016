package main

import (
	"fmt"
	"maps"
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

func get_abba_codes(word string) map[string]bool {
	n := len(word)

	if n < 3 {
		return make(map[string]bool)
	}

	babs := make(map[string]bool)
	for index := range n - 3 + 1 {
		if word[index] == word[index+2] && word[index] != word[index+1] {
			babs[word[index:index+3]] = true
		}
	}
	return babs
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

func supports_ssl(ip string) bool {
	outers, hypernets := parse_ip(ip)

	abba_in_outer := make(map[string]bool)
	for _, outer := range outers {
		maps.Copy(abba_in_outer, get_abba_codes(outer))
	}

	abas := make(map[string]bool)
	for bab, _ := range abba_in_outer {
		abas[string(bab[1])+string(bab[0])+string(bab[1])] = true
	}

	abba_in_hypernet := make(map[string]bool)
	for _, hypernet := range hypernets {
		maps.Copy(abba_in_hypernet, get_abba_codes(hypernet))
	}

	// one intersection is enough
	for k_abba, _ := range abas {
		_, k_abba_in_hypernet := abba_in_hypernet[k_abba]

		if k_abba_in_hypernet {
			return true
		}
	}
	for k_hyper, _ := range abba_in_hypernet {
		_, k_hyper_in_abas := abas[k_hyper]

		if k_hyper_in_abas {
			return true
		}
	}
	return false
}

func solve(data []string) int {
	supported := 0

	for _, ip := range data {
		if supports_ssl(ip) {
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
	fmt.Println(solution("./input.txt")) // 242
}
