import re
from itertools import permutations
from typing import Dict, List, Match, Optional, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def scramble(data: List[str], password: Tuple[str, ...]) -> str:

    letter_mapping: Dict[str, int] = {}
    index_mapping: Dict[int, str] = {}
    for index, char in enumerate(password):
        letter_mapping[char] = index
        index_mapping[index] = char

    re_swap_pos: str = r"swap position (\d) with position (\d)"
    re_swap_letter: str = r"swap letter (\w) with letter (\w)"
    re_rotate_lr: str = r"rotate (left|right) (\d) step"
    re_rotate_position: str = r"rotate based on position of letter (\w)"
    re_reverse: str = r"reverse positions (\d) through (\d)"
    re_move: str = r"move position (\d) to position (\d)"

    for line in data:
        for L, i in letter_mapping.items():
            assert index_mapping[i] == L

        for i, L in index_mapping.items():
            assert letter_mapping[L] == i

        index1: int
        index2: int
        letter: str
        letter1: str
        letter2: str

        matches: Optional[Match[str]] = re.match(re_swap_pos, line)
        if matches:
            index1 = int(matches.group(1))
            index2 = int(matches.group(2))

            letter1 = index_mapping[index1]
            letter2 = index_mapping[index2]

            letter_mapping[letter1] = index2
            letter_mapping[letter2] = index1

            index_mapping[index1] = letter2
            index_mapping[index2] = letter1
            continue

        matches = re.match(re_swap_letter, line)
        if matches:
            letter1 = matches.group(1)
            letter2 = matches.group(2)

            index1 = letter_mapping[letter1]
            index2 = letter_mapping[letter2]

            letter_mapping[letter1] = index2
            letter_mapping[letter2] = index1

            index_mapping[index1] = letter2
            index_mapping[index2] = letter1
            continue

        steps: int
        new_index: int

        matches = re.match(re_rotate_lr, line)
        if matches:
            direction: str = matches.group(1)
            steps = int(matches.group(2))

            incr: int
            if direction == "right":
                incr = 1
            else:
                incr = -1

            for letter_, index in letter_mapping.items():
                new_index = (letter_mapping[letter_] + (incr * steps)) % len(
                    letter_mapping
                )
                letter_mapping[letter_] = new_index
                index_mapping[new_index] = letter_

            continue

        matches = re.match(re_rotate_position, line)
        if matches:
            letter = matches.group(1)
            index = letter_mapping[letter]

            if index >= 4:
                steps = 1 + index + 1
            else:
                steps = 1 + index

            for letter, index in letter_mapping.items():
                new_index = (letter_mapping[letter] + steps) % len(letter_mapping)
                letter_mapping[letter] = new_index
                index_mapping[new_index] = letter

            continue

        matches = re.match(re_reverse, line)
        if matches:
            start: int = int(matches.group(1))
            end: int = int(matches.group(2))

            length = end - start + 1
            for i in range(length // 2):
                letter1 = index_mapping[start + i]
                letter2 = index_mapping[end - i]

                index1 = letter_mapping[letter1]
                index2 = letter_mapping[letter2]

                letter_mapping[letter1] = index2
                letter_mapping[letter2] = index1

                index_mapping[index1] = letter2
                index_mapping[index2] = letter1

            continue

        matches = re.match(re_move, line)
        if matches:
            index1 = int(matches.group(1))
            index2 = int(matches.group(2))

            letter_to_move: str = index_mapping[index1]

            if index2 >= index1:

                new_letter_mapping = letter_mapping.copy()
                new_index_mapping = index_mapping.copy()

                for i in range(index1 + 1, index2 + 1):
                    letter = index_mapping[i]
                    new_index = letter_mapping[letter] - 1
                    new_letter_mapping[letter] = new_index
                    new_index_mapping[new_index] = letter

                new_letter_mapping[letter_to_move] = index2
                new_index_mapping[index2] = letter_to_move

                letter_mapping = new_letter_mapping
                index_mapping = new_index_mapping

            else:
                new_letter_mapping = letter_mapping.copy()
                new_index_mapping = index_mapping.copy()
                for i in range(index2, index1):
                    letter = index_mapping[i]
                    new_index = letter_mapping[letter] + 1
                    new_letter_mapping[letter] = new_index
                    new_index_mapping[new_index] = letter

                new_letter_mapping[letter_to_move] = index2
                new_index_mapping[index2] = letter_to_move

                letter_mapping = new_letter_mapping
                index_mapping = new_index_mapping

            continue

    output: List[str] = []
    for i in range(len(letter_mapping)):
        output.append(index_mapping[i])

    return "".join(output)


def solution(filename: str, password: str) -> str:
    functions: List[str] = parse(filename)

    initial = ["a", "b", "c", "d", "e", "f", "g", "h"]
    n: int = len(initial)

    for p in permutations(initial, n):
        up = scramble(functions, p)
        if up == password:
            return "".join(p)

    return ""


if __name__ == "__main__":
    print(solution("./input.txt", "fbgdceah"))  # 0
