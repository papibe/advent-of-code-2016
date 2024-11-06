import hashlib
from typing import List


def md5_hash(string: str) -> str:
    # Create an MD5 hash object
    hash_object = hashlib.md5(string.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    return hex_dig


def solve(base: str) -> str:
    password: List[str] = []

    index: int = 0

    while len(password) < 8:
        while not (hash_ := md5_hash(base + str(index))).startswith("00000"):
            index += 1

        password.append(hash_[5])
        index += 1

    return "".join(password)


if __name__ == "__main__":
    print(solve("abc"))  # 18f47a30
    print(solve("cxdnnyjw"))  # f77a0e6e
