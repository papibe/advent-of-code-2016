import re


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()
    return data


def uncompress(sequence: str) -> int:
    marker_regex: str = r"\((\d+)x(\d+)\)"
    output_len: int = 0

    while True:
        matches = re.search(marker_regex, sequence)
        if matches:
            start_index = matches.start()
            end_index = matches.end()
            regex_length = len(matches.group(0))
            amount: int = int(matches.group(1))
            times: int = int(matches.group(2))
        else:
            # no marker left
            output_len += len(sequence)
            break

        # add prefix with no marker
        output_len += start_index

        # calculate indexes for uncompress nested sequence
        next_start_index: int = start_index + regex_length
        next_end_index: int = end_index + amount

        output_len += times * uncompress(sequence[next_start_index:next_end_index])

        # adjust string for next call
        sequence = sequence[next_end_index:]

    return output_len


def solution(filename: str) -> int:
    sequence: str = parse(filename)
    return uncompress(sequence)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 10774309173
