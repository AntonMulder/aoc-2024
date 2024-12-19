from queue import PriorityQueue


def solve(input_data):
    # Prepare data.
    walls = []
    max_x = 0
    max_y = 0
    for wall in input_data.split("\n"):
        x, y = map(int, wall.split(","))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        walls.append((y, x))
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

    epoch = len(walls) // 2
    step = epoch
    not_solved = set()
    while True:
        run_walls = walls[:epoch]

        # Find shortest path.
        queue = PriorityQueue()
        queue.put((0, start))
        visited = set()
        solved = False
        while not queue.empty():
            score, point = queue.get()
            for neighbor in neighbors(point):
                if neighbor == finish:
                    solved = True

                if neighbor not in visited and neighbor not in run_walls:
                    visited.add(neighbor)
                    queue.put((score + 1, neighbor))

        step = max(step // 2, 1)
        if solved:
            if epoch + 1 in not_solved:
                return f"{walls[epoch][1]},{walls[epoch][0]}"
            epoch += step
        else:
            not_solved.add(epoch)
            epoch -= step


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
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_solve():
    assert solve(EXAMPLE) == "6,1"
