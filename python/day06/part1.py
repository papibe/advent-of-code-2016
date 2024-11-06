from typing import Dict, List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def solve(data: List[str]) -> str:
    frequencies: List[Dict[str, int]] = [{} for _ in range(len(data[0]))]

    for word in data:
        for index, char in enumerate(word):
            frequencies[index][char] = frequencies[index].get(char, 0) + 1

    message: List[str] = []

    for frequency in frequencies:
        max_freq: int = float("-inf")  # type: ignore
        max_char: str = ""

        for char, freq in frequency.items():
            if freq > max_freq:
                max_freq = freq
                max_char = char

        message.append(max_char)

    return "".join(message)


def solution(filename: str) -> str:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # easter
    print(solution("./input.txt"))  # umejzgdw
