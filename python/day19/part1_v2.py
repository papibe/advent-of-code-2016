from math import floor, log2


def josephus(n: int) -> int:
    L: int = n - 2 ** (floor(log2(n)))
    return 2 * L + 1


def solution(number_of_elves: int) -> int:
    return josephus(number_of_elves)


if __name__ == "__main__":
    print(solution(3014387))  # 1834471
