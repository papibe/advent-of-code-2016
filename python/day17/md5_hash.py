import hashlib


def md5_short_hash(string: str) -> str:
    # Create an MD5 hash object
    hash_object = hashlib.md5(string.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    return hex_dig[:4]
