package main

import (
	"fmt"
	"testing"
)

func TestGotAbba(t *testing.T) {
	testCases := []struct {
		word     string
		expected bool
	}{
		{"abba", true},
		{"xyyx", true},
		{"yxxy", true},
		{"aaaa", false},
		{"bddb", true},
		{"ioxxoj", true},
		{"iasoxxo", true},
		{"oxxoias", true},
		{"123", false},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%v", tc.word, tc.expected), func(t *testing.T) {
			result := got_abba(tc.word)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}

func TestSupportTLS(t *testing.T) {
	testCases := []struct {
		ip       string
		expected bool
	}{
		{"abba[mnop]qrst", true},
		{"abcd[bddb]xyyx", false},
		{"aaaa[qwer]tyui", false},
		{"ioxxoj[asdfgh]zxcvbn", true},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%v", tc.ip, tc.expected), func(t *testing.T) {
			result := supports_tls(tc.ip)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}
