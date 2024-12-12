from collections import defaultdict


def solve(input_data):
    # Create list of stones.
    stones = defaultdict(lambda: 0)
    for stone in map(int, input_data.split(" ")):
        stones[stone] += 1

    for _ in range(25):
        new_stones = defaultdict(lambda: 0)
        for stone, value in stones.items():
            if stone == 0:
                new_stones[1] += value
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                left, right = (
                    int(stone[: len(stone) // 2]),
                    int(stone[len(stone) // 2 :]),
                )
                new_stones[left] += value
                new_stones[right] += value
            else:
                new_stones[stone * 2024] += value
        stones = new_stones

    return sum(stones[x] for x in stones.keys())


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = "125 17"


def test_solve():
    assert solve(EXAMPLE) == 55312
