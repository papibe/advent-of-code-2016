package main

import (
	"fmt"
	"testing"
)

func TestSupportSSL(t *testing.T) {
	testCases := []struct {
		ip       string
		expected bool
	}{
		{"aba[bab]xyz", true},
		{"xyx[xyx]xyx", false},
		{"aaa[kek]eke", true},
		{"zazbz[bzb]cdb", true},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%v", tc.ip, tc.expected), func(t *testing.T) {
			result := supports_ssl(tc.ip)
			if result != tc.expected {
				t.Errorf("got %v; want %v", result, tc.expected)
			}
		})
	}
}
