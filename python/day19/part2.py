def joseph_180(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 3

    mod: int = n % 3
    if mod == 0:
        return 3 * joseph_180(n // 3)

    length: int = (n + 2) // 3
    sub_problem: int = joseph_180(length)
    half: int = length // 2

    if sub_problem <= half:
        return (3 * sub_problem) - (3 - mod)
    else:
        return (3 * sub_problem) - 2 * (3 - mod)


def solution(number_of_elves: int) -> int:
    return joseph_180(number_of_elves)


if __name__ == "__main__":
    assert solution(5) == 2
    assert solution(3014387) == 1420064
