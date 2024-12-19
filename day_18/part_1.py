from queue import PriorityQueue


def solve(input_data):
    # Prepare data.
    walls = set()
    max_x = 0
    max_y = 0
    for wall in input_data.split("\n")[:1024]:
        x, y = map(int, wall.split(","))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        walls.add((y, x))
    start = (0, 0)
    finish = (max_y, max_x)

    def neighbors(point):
        points = (
            (point[0], point[1] - 1),  # Left.
            (point[0] - 1, point[1]),  # Up.
            (point[0], point[1] + 1),  # Right.
            (point[0] + 1, point[1]),  # Down
        )
        for y, x in points:
            if 0 <= y <= max_y and 0 <= x <= max_y:
                yield y, x

    # Find shortest path.
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    while True:
        score, point = queue.get()
        for x in neighbors(point):
            if x == finish:
                return score + 1

            if x not in visited and x not in walls:
                visited.add(x)
                queue.put((score + 1, x))


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1"""


def test_solve():
    assert solve(EXAMPLE) == 22
