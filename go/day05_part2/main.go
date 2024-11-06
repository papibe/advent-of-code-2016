package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func md5_hash(text string) string {
	hash := md5.Sum([]byte(text))
	// fmt.Printf("%T\n", hash)
	return hex.EncodeToString(hash[:])
}

func is_good_hash(s string) bool {
	for i := 0; i < 5; i++ {
		if s[i] != 48 {
			return false
		}
	}
	return true
}

func solve(base string) string {
	password := []string{" ", " ", " ", " ", " ", " ", " ", " "}
	index := 0
	counter := 0

	for counter < 8 {
		index_str := strconv.Itoa(index)
		hash := md5_hash(base + index_str)
		for !is_good_hash(hash) {
			index++
			index_str = strconv.Itoa(index)
			hash = md5_hash(base + index_str)
		}
		position, _ := strconv.ParseInt(string(hash[5]), 16, 32)
		if 0 <= position && position < 8 && password[position] == " " {
			password[position] = string(hash[6])
			counter++
		}
		index++
	}
	return strings.Join(password, "")
}

func main() {
	fmt.Println(solve("abc"))      // 05ace8e3
	fmt.Println(solve("cxdnnyjw")) // 999828ec
}
