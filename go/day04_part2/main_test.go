package main

import (
	"fmt"
	"testing"
)

func TestDecrypt(t *testing.T) {
	testCases := []struct {
		name     string
		sector   int
		expected string
	}{
		{"qzmt-zixmtkozy-ivhz", 343, "very encrypted name"},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s-%d_should_be_%s", tc.name, tc.sector, tc.expected), func(t *testing.T) {
			room := Room{"", tc.name, tc.sector, ""}
			result := room.decrypt()
			if result != tc.expected {
				t.Errorf("got %s; want %s", result, tc.expected)
			}
		})
	}
}
