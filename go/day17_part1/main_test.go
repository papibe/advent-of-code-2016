package main

import (
	"fmt"
	"testing"
)

func TestMD5(t *testing.T) {
	testCases := []struct {
		str      string
		expected string
	}{
		{"hijkl", "ced9"},
		{"hijklD", "f2bc"},
		{"hijklDR", "5745"},
		{"hijklDU", "528e"},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%v", tc.str, tc.expected), func(t *testing.T) {

			result := md5_hash(tc.str)
			if result[:4] != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}

func TestSolution(t *testing.T) {
	testCases := []struct {
		str      string
		expected string
	}{
		{"ihgpwlah", "DDRRRD"},
		{"kglvqrro", "DDUDRLRRUDRD"},
		{"ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%v", tc.str, tc.expected), func(t *testing.T) {

			result := solution(tc.str)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}
