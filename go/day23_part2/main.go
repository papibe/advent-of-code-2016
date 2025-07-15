package main

import (
	"fmt"
)

func main() {
	a, b, c, d := 0, 0, 0, 0

	a = 12
	b = a
	b--

	for {
		d = a
		a = 0
		c = b
		a += c * d

		b--
		c = b
		d = c

		c += d

		if -16 <= c && c <= 9 {
			fmt.Println("Toggle instruction", c)
		}

		if c == 2 {
			break
		}
	}

	fmt.Println("Registers after main loop", a, b, c, d)
	a += 72 * 71

	fmt.Println("Registers at the end", a, b, c, d)
	fmt.Println("a =", a)
}
