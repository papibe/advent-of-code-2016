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
		{"(3x3)XYZ", 9},
		{"X(8x2)(3x3)ABCY", 20},
		{"(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920},
		{"(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%d", tc.sequence, tc.expected), func(t *testing.T) {
			result := uncompress([]byte(tc.sequence))
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
