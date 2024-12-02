def solve(input_data):
    left = []
    right = []

    for line in input_data.splitlines():
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)

    left.sort()
    right.sort()

    return sum(abs(x - y) for x, y in zip(left, right, strict=False))


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
    assert solve(EXAMPLE) == 11
