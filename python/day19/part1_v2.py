from math import log2, floor

def josephus(n: int) -> int:
    l: int = (n - 2 ** (floor(log2(n))))
    return 2 * l + 1

def solution(number_of_elves: int) -> int:
    return josephus(number_of_elves)


if __name__ == "__main__":
    print(solution(5))  # 3
    print(solution(3014387))  # 1834471
