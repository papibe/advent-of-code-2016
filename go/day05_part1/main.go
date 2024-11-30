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
	password := []string{}
	index := 0

	for len(password) < 8 {
		index_str := strconv.Itoa(index)
		hash := md5_hash(base + index_str)
		for !is_good_hash(hash) {
			index++
			index_str = strconv.Itoa(index)
			hash = md5_hash(base + index_str)
		}
		password = append(password, string(hash[5]))
		index++
	}
	return strings.Join(password, "")
}

func main() {
	fmt.Println(solve("abc"))      // 18f47a30
	fmt.Println(solve("cxdnnyjw")) // f77a0e6e
}
