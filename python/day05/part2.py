import hashlib
from typing import List


def md5_hash(string: str) -> str:
    # Create an MD5 hash object
    hash_object = hashlib.md5(string.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    return hex_dig


def solve(base: str) -> str:
    password: List[str] = [" "] * 8

    index: int = 0
    counter: int = 0

    while counter < 8:
        while not (hash_ := md5_hash(base + str(index))).startswith("00000"):
            index += 1

        position: int = int(hash_[5], 16)
        if 0 <= position < 8 and password[position] == " ":
            password[position] = hash_[6]
            counter += 1

        index += 1

    return "".join(password)


if __name__ == "__main__":
    print(solve("abc"))  # 05ace8e3
    print(solve("cxdnnyjw"))  # 999828ec
