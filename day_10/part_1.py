def solve(input_data):
    # Create area and starting points.
    area = []
    starting_points = []
    for y, line in enumerate(input_data.split("\n")):
        number_line = list(map(int, line))
        for x, value in enumerate(number_line):
            if value == 0:
                starting_points.append((y, x))
        area.append(number_line)

    def neighbors(point):
        points = (
            (point[0], point[1] - 1),  # Left.
            (point[0] - 1, point[1]),  # Up.
            (point[0], point[1] + 1),  # Right.
            (point[0] + 1, point[1]),  # Down
        )
        for y, x in points:
            if 0 <= y < len(area) and 0 <= x < len(area[0]):
                yield y, x

    # Go through all points to explore.
    answer = 0
    for starting_point in starting_points:
        tops = set()
        trail = [starting_point]

        while trail:
            point = trail.pop(0)
            if area[point[0]][point[1]] == 9:
                tops.add(point)
            else:
                # Get neighbors.
                next_value = area[point[0]][point[1]] + 1

                for neighbor in neighbors(point):
                    if area[neighbor[0]][neighbor[1]] == next_value:
                        trail.append(neighbor)
        answer += len(tops)

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_solve():
    assert solve(EXAMPLE) == 36
