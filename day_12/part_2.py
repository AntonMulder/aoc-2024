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

    def corner_including_neighbors(point):
        points = (
            (
                (point[0], point[1] - 1),  # West
                (point[0] - 1, point[1] - 1),  # North-West.
                (point[0] - 1, point[1]),  # North.
            ),
            (
                (point[0] - 1, point[1]),  # North.
                (point[0] - 1, point[1] + 1),  # North-East.
                (point[0], point[1] + 1),  # East.
            ),
            (
                (point[0], point[1] + 1),  # East.
                (point[0] + 1, point[1] + 1),  # East-south.
                (point[0] + 1, point[1]),  # South.
            ),
            (
                (point[0] + 1, point[1]),  # South.
                (point[0] + 1, point[1] - 1),  # South-West.
                (point[0], point[1] - 1),  # West.
            ),
        )
        yield from points

    # Compute answer. Number of sides is equal to the number of corners.
    answer = 0
    for location in region.keys():
        if location not in visited:
            sub_region = find_region(location)
            corners = 0
            for plant in sub_region:
                for first, corner, second in corner_including_neighbors(plant):
                    # A corner has horizontal/vertical different neighbor.
                    # Or when the same, diagonal neighbor should be different.
                    if (first not in sub_region and second not in sub_region) or (
                        first in sub_region
                        and second in sub_region
                        and corner not in sub_region
                    ):
                        corners += 1
            answer += corners * len(sub_region)

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
    assert solve(EXAMPLE) == 1206
