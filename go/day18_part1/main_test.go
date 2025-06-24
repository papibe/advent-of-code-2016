package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		tiles    string
		rows     int
		expected int
	}{
		{"..^^.", 3, 6},
		{".^^.^.^^^^", 10, 38},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%v", tc.tiles, tc.expected), func(t *testing.T) {
			result := solve(tc.tiles, tc.rows)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}
