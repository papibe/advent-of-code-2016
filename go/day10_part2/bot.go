package main

import (
	"sort"
)

type Bot struct {
	values []int
}

func (b *Bot) receive_value(value int) {
	if len(b.values) >= 2 {
		panic("already 3 values")
	}

	b.values = append(b.values, value)
	sort.Ints(b.values)
}

func (b *Bot) give_low() int {
	if len(b.values) == 0 {
		panic("no values to give")
	}

	value := b.values[0]
	b.values = b.values[1:]

	return value
}

func (b *Bot) give_high() int {
	if len(b.values) == 0 {
		panic("no values to give")
	}

	value := b.values[len(b.values)-1]
	b.values = b.values[:len(b.values)-1]

	return value
}

func (b *Bot) may_proceed() bool {
	return len(b.values) == 2
}

func NewBot() *Bot {
	return &Bot{[]int{}}
}
