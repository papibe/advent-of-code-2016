import re
from typing import List, Match, Optional, Set, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def get_abba_codes(word: str) -> Set[str]:
    n: int = len(word)

    if n < 3:
        return set()

    babs = set()

    for index in range(n - 3 + 1):
        if word[index] == word[index + 2] and word[index] != word[index + 1]:
            babs.add(word[index : index + 3])

    return babs


def parse_ip(ip: str) -> Tuple[List[str], List[str]]:

    outers: List[str] = []
    hypernets: List[str] = []

    outer_regex: str = r"^\w+"
    hypernet_regex: str = r"^\[(\w+)\]"

    while len(ip) > 0:
        outer_matches: Optional[Match[str]] = re.search(outer_regex, ip)
        hypernet_matches: Optional[Match[str]] = re.search(hypernet_regex, ip)

        a_match: str

        if outer_matches:
            a_match = outer_matches.group()
            outers.append(a_match)
            ip = ip[len(a_match) :]

        elif hypernet_matches:
            a_match = hypernet_matches.group(1)
            hypernets.append(a_match)
            ip = ip[len(a_match) + 2 :]

    return outers, hypernets


def supports_ssl(ip: str) -> bool:
    outers, hypernets = parse_ip(ip)

    abba_in_outer: Set[str] = set()
    for outer in outers:
        abba_in_outer |= get_abba_codes(outer)

    abas = set()
    for bab in abba_in_outer:
        abas.add(bab[1] + bab[0] + bab[1])

    abba_in_hypernet: Set[str] = set()
    for hypernet in hypernets:
        abba_in_hypernet |= get_abba_codes(hypernet)

    corresponding = abas & abba_in_hypernet

    return len(corresponding) > 0


def solve(data: List[str]) -> int:
    supported: int = 0

    for ip in data:
        if supports_ssl(ip):
            supported += 1

    return supported


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 242
