def solve(input_data):
    # Create data to work with.
    data = input_data.split("\n")
    region = {}
    for y, line in enumerate(data):
        for x, plant in enumerate(line):
            region[(y, x)] = plant
    visited = set()

    # Get neighbor locations.
    height = len(data[0])
    width = len(data[0])

    def neighbors(point):
        points = (
            (point[0], point[1] - 1),  # Left.
            (point[0] - 1, point[1]),  # Up.
            (point[0], point[1] + 1),  # Right.
            (point[0] + 1, point[1]),  # Down
        )
        for y, x in points:
            if 0 <= y < height and 0 <= x < width:
                yield y, x

    # Recursive function to find plants who are in the same region.
    def find_region(point):
        if point not in visited:
            visited.add(point)

            sub_region = [point]
            for neighbor in neighbors(point):
                # Same region.
                if region[neighbor] == region[point]:
                    sub_region += find_region(neighbor)
            return sub_region
        return []

    # Compute answer
    answer = 0
    for location in region.keys():
        if location not in visited:
            sub_region = find_region(location)

            plant_sides = 0
            for plant in sub_region:
                # When plant has a neighbor that is in the sub region,
                # no fence is needed.
                sides = 4
                for neighbor in neighbors(plant):
                    if neighbor in sub_region:
                        sides -= 1
                plant_sides += sides
            answer += plant_sides * len(sub_region)
    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_solve():
    assert solve(EXAMPLE) == 1930
