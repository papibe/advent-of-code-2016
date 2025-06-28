import re
from typing import Dict, List, Match, Optional


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def solve(data: List[str], password: str) -> str:
    p: List[str] = list(password)

    letter_mapping: Dict[str, int] = {}
    index_mapping: Dict[int, str] = {}
    for index, char in enumerate(p):
        letter_mapping[char] = index
        index_mapping[index] = char

    re_swap_pos: str = r"swap position (\d) with position (\d)"
    re_swap_letter: str = r"swap letter (\w) with letter (\w)"
    re_rotate_lr: str = r"rotate (left|right) (\d) step"
    re_rotate_position: str = r"rotate based on position of letter (\w)"
    re_reverse: str = r"reverse positions (\d) through (\d)"
    re_move: str = r"move position (\d) to position (\d)"

    counter = 0

    for line in reversed(data):
        counter += 1

        # check
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
            if direction == "left":
                incr = 1
            else:
                incr = -1

            for letter, index in letter_mapping.items():
                new_index = (letter_mapping[letter] + (incr * steps)) % len(
                    letter_mapping
                )
                letter_mapping[letter] = new_index
                index_mapping[new_index] = letter

            continue

        matches = re.match(re_rotate_position, line)
        if matches:
            solutions = []
            rotate_at_letter: str = matches.group(1)

            pre_rotations = []

            for _steps in range(1, len(letter_mapping) + 1):
                new_letter_mapping = letter_mapping.copy()
                new_index_mapping = index_mapping.copy()

                for letter, index in letter_mapping.items():
                    new_index = (letter_mapping[letter] - _steps) % len(letter_mapping)
                    new_letter_mapping[letter] = new_index
                    new_index_mapping[new_index] = letter

                output: List[str] = []
                for i in range(len(letter_mapping)):
                    output.append(new_index_mapping[i])

                pre_rotations.append("".join(output))

                index_: int = new_letter_mapping[rotate_at_letter]

                if index_ >= 4:
                    steps = 1 + index_ + 1
                else:
                    steps = 1 + index_

                rotation_letter_mapping = new_letter_mapping.copy()
                rotation_index_mapping = new_index_mapping.copy()

                for letter, index in new_letter_mapping.items():
                    new_index = (new_letter_mapping[letter] + steps) % len(
                        new_letter_mapping
                    )
                    rotation_letter_mapping[letter] = new_index
                    rotation_index_mapping[new_index] = letter

                output2: List[str] = []
                for i in range(len(rotation_letter_mapping)):
                    output2.append(rotation_index_mapping[i])

                if rotation_letter_mapping == letter_mapping:
                    solutions.append(
                        (
                            new_letter_mapping.copy(),
                            new_index_mapping.copy(),
                            "".join(output),
                            index_,
                            steps,
                            "".join(output2),
                        )
                    )
            assert len(solutions) == 1

            if len(solutions) == 1:
                letter_mapping = solutions[0][0]
                index_mapping = solutions[0][1]

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
            index2 = int(matches.group(1))
            index1 = int(matches.group(2))

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

    final_output: List[str] = []
    for i in range(len(letter_mapping)):
        final_output.append(index_mapping[i])

    return "".join(final_output)


def solution(filename: str, password: str) -> str:
    functions: List[str] = parse(filename)
    return solve(functions, password)


if __name__ == "__main__":
    print(solution("./input.txt", "fbgdceah"))  # egcdahbf
