package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		n        int
		expected int
	}{
		{1, 1},
		{2, 1},
		{3, 3},
		{4, 1},
		{5, 2},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%d", tc.n, tc.expected), func(t *testing.T) {
			result := josephus_180(tc.n)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
