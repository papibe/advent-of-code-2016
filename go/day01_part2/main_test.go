package main

import (
	"fmt"
	"testing"
)

var r8 = Instruction{"R", 8}
var r4 = Instruction{"R", 4}

func TestSolve(t *testing.T) {
	testCases := []struct {
		instructions []Instruction
		expected     int
	}{
		{[]Instruction{r8, r4, r4, r8}, 4},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%v_should_be_%d", tc.instructions, tc.expected), func(t *testing.T) {
			result := solve(tc.instructions, Location{0, 0, Direction{-1, 0}})
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
