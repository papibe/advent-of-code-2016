import re
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

class Bot:
    def __init__(self) -> None:
        self.values: List[int] = []

    def receive_value(self, value: int) -> None:
        if len(self.values) >= 2:
            raise Exception("already 3 values")

        self.values.append(value)
        self.values.sort()

    def give_low(self) -> int:
        if not self.values:
            raise Exception("no values to give")

        return self.values.pop(0)


    def give_high(self) -> int:
        if not self.values:
            raise Exception("no values to give")

        return self.values.pop()

    def may_procede(self) -> bool:
        return len(self.values) == 2

    def __repr__(self) -> str:
        return f"{self.values}"


def parse(filename: str, value1: int, value2: int) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    value_regex: str = r"value (\d+) goes to bot (\d+)"
    bot_regex: str = r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"

    bots: Dict[int, Bot] = {}
    outputs: Dict[int, int] = {}

    rules: Dict[int, str] = {}


    # get initial values
    for line in data:
        value_match: Optional[Match[str]] = re.match(value_regex, line)
        bot_match: Optional[Match[str]] = re.match(bot_regex, line)

        if value_match:
            value: int = int(value_match.group(1))
            bot_number: int = int(value_match.group(2))
            if bot_number not in bots:
                bots[bot_number] = Bot()
            bots[bot_number].receive_value(value)

        elif bot_match:
            giving_bot: int = int(bot_match.group(1))
            receiving_low_identity: str = bot_match.group(2)
            receiving_low_number: int = int(bot_match.group(3))
            receiving_high_identity: str = bot_match.group(4)
            receiving_high_number: int = int(bot_match.group(5))

            if giving_bot not in bots:
                bots[giving_bot] = Bot()

            if receiving_low_identity == "bot" and receiving_low_number not in bots:
                bots[receiving_low_number] = Bot()

            if receiving_high_identity == "bot" and receiving_high_number not in bots:
                bots[receiving_high_number] = Bot()

            rules[giving_bot] = line

    print(bots)

    # run transfer rules
    # while any(len(bot) == 2 for bot in bots):
    while True:
        for index, bot in bots.items():
            if bot.may_procede():
                break
        else:
            break

        print(f"procesing: {index}, {bot}")
        print(f"{rules[index] = }")

        bot_match: Optional[Match[str]] = re.match(bot_regex, rules[index])

        if bot_match:

            giving_bot: int = int(bot_match.group(1))
            receiving_low_number: int = int(bot_match.group(3))
            receiving_high_number: int = int(bot_match.group(5))

            receiving_low_identity: str = bot_match.group(2)
            receiving_high_identity: str = bot_match.group(4)

            print(f"{giving_bot = }, {bots[giving_bot]}")

            # if bots[giving_bot].values == [value1, value2]:
            #     return giving_bot


            if receiving_low_identity == "output":
                outputs[receiving_low_number] = bots[giving_bot].give_low()
            else:
                bots[receiving_low_number].receive_value(bots[giving_bot].give_low())

            if receiving_high_identity == "output":
                outputs[receiving_high_number] = bots[giving_bot].give_high()
            else:
                bots[receiving_high_number].receive_value(bots[giving_bot].give_high())


            print(bots)
            print()


    for k in sorted(outputs.keys()):
        print(k, outputs[k])

    return outputs[0] * outputs[1] * outputs[2]


# def solve(data: List[str]) -> int:
#     total_sum: int = 0

#     for row in data:
#         pass

    return total_sum


def solution(filename: str, value1: int, value2: int) -> int:
    return parse(filename, value1, value2)


if __name__ == "__main__":
    # print(solution("./example.txt", 2, 5))  # 0
    print(solution("./input.txt", 17, 61))  # 0