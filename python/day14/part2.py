import hashlib
from typing import Dict, List, Set, Tuple


def stretch_hash(string: str, times: int) -> str:
    for _ in range(times + 1):
        hash_object = hashlib.md5(string.encode())
        string = hash_object.hexdigest()

    return string


def count_repetitions(s: str) -> Tuple[bool, str, List[str]]:
    repeated: int = 1
    previous_char: str = ""

    triple_char: str = ""
    found3: bool = False

    repeated_fives: List[str] = []

    for char in s:
        if char == previous_char:
            repeated += 1
        else:
            repeated = 1

        if repeated == 3 and not triple_char:
            triple_char = char
            found3 = True

        if repeated == 5:
            repeated_fives.append(char)

        previous_char = char

    return found3, triple_char, repeated_fives


def solution(salt: str) -> int:
    index: int = 0
    keys: Set[int] = set()

    candidates: Dict[str, List[int]] = {}

    while True:
        hash_: str = stretch_hash(salt + str(index), 2016)
        found3, char3, repeated_fives = count_repetitions(hash_)

        if found3:
            if char3 not in candidates:
                candidates[char3] = []

            candidates[char3].append(index)

        for char in repeated_fives:

            if char in candidates:
                for previous_index in candidates[char]:
                    if index > previous_index and index - previous_index <= 1000:
                        keys.add(previous_index)
                        if len(keys) == 64:
                            return previous_index
        index += 1

    return -1


if __name__ == "__main__":
    # print(solution("abc"))  # 22551
    print(solution("cuanljph"))  # 20606
