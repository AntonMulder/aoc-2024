import re

PATTERN = (
    r"(?P<do>do)\(\)|(?P<mul>mul)\((?P<left>\d+),(?P<right>\d+)\)|(?P<dont>don't)\(\)"
)


def solve(input_data):
    answer = 0
    multiply = True
    for match in re.finditer(PATTERN, input_data):
        if match.group("do"):
            multiply = True
        elif match.group("dont"):
            multiply = False
        elif match.group("mul") and multiply:
            multiply = True
            answer += int(match.group("left")) * int(match.group("right"))

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_solve():
    assert solve(EXAMPLE) == 48
