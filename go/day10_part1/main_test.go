package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		sequence string
		expected int
	}{
		{"ADVENT", 6},
		{"A(1x5)BC", 7},
		{"(3x3)XYZ", 9},
		{"A(2x2)BCD(2x2)EFG", 11},
		{"(6x1)(1x3)A", 6},
		{"X(8x2)(3x3)ABCY", 18},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%d", tc.sequence, tc.expected), func(t *testing.T) {
			result := solve(tc.sequence)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
