from collections import defaultdict


def solve(input_data):
    left = []
    right = defaultdict(lambda: 0)

    for line in input_data.splitlines():
        x, y = map(int, line.split())
        left.append(x)
        right[y] += 1

    return sum(x * right[x] for x in left)


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_solve():
    assert solve(EXAMPLE) == 31
