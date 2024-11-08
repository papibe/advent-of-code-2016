package main

import (
	"fmt"
	"testing"
)

var r2 = Instruction{"R", 2}
var l3 = Instruction{"L", 3}
var r5 = Instruction{"R", 5}
var l5 = Instruction{"L", 5}
var r3 = Instruction{"R", 3}

func TestSolve(t *testing.T) {
	testCases := []struct {
		instructions []Instruction
		expected     int
	}{
		{[]Instruction{r2, l3}, 5},
		{[]Instruction{r2, r2, r2}, 2},
		{[]Instruction{r5, l5, r5, r3}, 12},
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
