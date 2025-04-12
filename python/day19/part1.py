def josephus(n: int) -> int:
    if n == 1:
        return 1

    if n % 2 == 0:
        return 2 * josephus(n // 2) - 1
    else:
        return 2 * josephus(n // 2) + 1


def solution(number_of_elves: int) -> int:
    return josephus(number_of_elves)


if __name__ == "__main__":
    print(solution(5))  # 3
    print(solution(3014387))  # 1834471
