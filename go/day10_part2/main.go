package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(filename string) (*map[int]*Bot, map[int]string) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	value_regex := regexp.MustCompile(`value (\d+) goes to bot (\d+)`)
	bot_regex := regexp.MustCompile(`bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)`)

	bots_ := make(map[int]*Bot)
	bots := &bots_
	rules := make(map[int]string)

	for _, line := range lines {
		value_match := value_regex.FindStringSubmatch(line)
		bot_match := bot_regex.FindStringSubmatch(line)

		if len(value_match) > 0 {
			value, _ := strconv.Atoi(value_match[1])
			bot_number, _ := strconv.Atoi(value_match[2])

			_, in_bots := (*bots)[bot_number]
			if !in_bots {
				(*bots)[bot_number] = NewBot()
			}
			(*bots)[bot_number].receive_value(value)

		} else { // bot_match
			giving_bot, _ := strconv.Atoi(bot_match[1])

			receiving_low_identity := bot_match[2]
			receiving_low_number, _ := strconv.Atoi(bot_match[3])
			receiving_high_identity := bot_match[4]
			receiving_high_number, _ := strconv.Atoi(bot_match[5])

			_, in_bots := (*bots)[giving_bot]
			if !in_bots {
				(*bots)[giving_bot] = NewBot()
			}

			_, receiving_low_number_in_bots := (*bots)[receiving_low_number]
			if receiving_low_identity == "bot" && !receiving_low_number_in_bots {
				(*bots)[receiving_low_number] = NewBot()
			}

			_, receiving_high_number_in_bots := (*bots)[receiving_high_number]
			if receiving_high_identity == "bot" && !receiving_high_number_in_bots {
				(*bots)[receiving_high_number] = NewBot()
			}

			rules[giving_bot] = line

		}
	}

	return bots, rules
}

func solve(bots *map[int]*Bot, rules map[int]string, value1, value2 int) int {

	bot_regex := regexp.MustCompile(`bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)`)
	outputs := make(map[int]int)

	for {
		index := -1
		found := false
		for i, bot := range *bots {
			if bot.may_proceed() {
				index = i
				found = true
				break
			}
		}
		if !found {
			break
		}

		bot_match := bot_regex.FindStringSubmatch(rules[index])

		if len(bot_match) > 0 {

			giving_bot, _ := strconv.Atoi(bot_match[1])

			receiving_low_identity := bot_match[2]
			receiving_low_number, _ := strconv.Atoi(bot_match[3])
			receiving_high_identity := bot_match[4]
			receiving_high_number, _ := strconv.Atoi(bot_match[5])

			// bot_values := (*bots)[giving_bot].values
			// _ = bot_values
			// if bot_values[0] == value1 && bot_values[1] == value2 {
			// 	return giving_bot
			// }

			if receiving_low_identity == "output" {
				bot := (*bots)[giving_bot]
				outputs[receiving_low_number] = bot.give_low()

			} else {
				giving_bot := (*bots)[giving_bot]
				low_value := giving_bot.give_low()

				receiving_bot := (*bots)[receiving_low_number]
				receiving_bot.receive_value(low_value)
			}

			if receiving_high_identity == "output" {
				bot := (*bots)[giving_bot]
				outputs[receiving_high_number] = bot.give_low()

			} else {
				giving_bot := (*bots)[giving_bot]
				high_value := giving_bot.give_high()

				receiving_bot := (*bots)[receiving_high_number]
				receiving_bot.receive_value(high_value)
			}

		}
	}

	return outputs[0] * outputs[1] * outputs[2]
}

func solution(filename string, value1, value2 int) int {
	bots, rules := parse(filename)
	return solve(bots, rules, value1, value2)
}

func main() {
	fmt.Println(solution("./input.txt", 17, 61)) // 2666
}
