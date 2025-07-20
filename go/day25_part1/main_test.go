package main

import (
	"testing"
)

func TestSolve(t *testing.T) {
	res := solution("./input.txt")
	expected := 189
	if expected != res {
		t.Fatalf("expected %d, got %d", expected, res)
	}
}
