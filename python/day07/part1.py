import re
from typing import List, Match, Optional, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def got_abba(word: str) -> bool:
    n: int = len(word)

    if n < 4:
        return False

    for index in range(n - 4 + 1):
        if (
            word[index] == word[index + 3]
            and word[index + 1] == word[index + 2]
            and word[index] != word[index + 1]
        ):
            return True

    return False


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


def supports_tls(ip: str) -> bool:

    outers, hypernets = parse_ip(ip)

    abba_in_outer: bool = False
    for outer in outers:
        abba_in_outer = abba_in_outer or got_abba(outer)

    abba_in_hypernet: bool = False
    for hypernet in hypernets:
        abba_in_hypernet = abba_in_hypernet or got_abba(hypernet)

    if abba_in_outer and not abba_in_hypernet:
        return True

    return False


def solve(data: List[str]) -> int:
    supported: int = 0

    for ip in data:
        if supports_tls(ip):
            supported += 1

    return supported


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 110
