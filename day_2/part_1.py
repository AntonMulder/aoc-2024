def is_valid(level):
    if level == sorted(level) or level == sorted(level, reverse=True):
        diff = (abs(y - x) for x, y in zip(level, level[1:]))

        if all(1 <= x <= 3 for x in diff):
            return True
    return False


def solve(input_data):
    valid = 0
    for line in input_data.splitlines():
        level = list(map(int, line.split()))

        if is_valid(level):
            valid += 1

    return valid


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_solve():
    assert solve(EXAMPLE) == 2
