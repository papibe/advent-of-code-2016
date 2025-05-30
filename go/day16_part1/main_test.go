package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		data     string
		expected string
	}{
		{"110010110100", "100"},
		{"10000011110010000111", "01100"},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%v", tc.data, tc.expected), func(t *testing.T) {
			data_list := []string{}
			for _, char := range tc.data {
				data_list = append(data_list, string(char))
			}
			result := check_sum(data_list)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}
