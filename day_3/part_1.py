import re


def solve(input_data):
    answer = 0

    for x in re.finditer(r"mul\((\d+),(\d+)\)", input_data):
        x, y = map(int, x.groups())
        answer += x * y

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_solve():
    assert solve(EXAMPLE) == 161
