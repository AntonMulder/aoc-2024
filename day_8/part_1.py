from collections import defaultdict
from itertools import combinations


def solve(input_data):
    antinodes = set()
    antennas = defaultdict(list)
    map = input_data.split("\n")

    # Get antenna locations.
    for y, line in enumerate(map):
        for x, possible_antena in enumerate(line):
            if possible_antena != ".":
                antennas[possible_antena].append((y, x))

    def is_valid(antinode):
        return 0 <= antinode[0] < len(map) and 0 <= antinode[1] < len(map[0])

    for _, v in antennas.items():
        for first, second in combinations(v, 2):
            delta_y = first[0] - second[0]
            delta_x = first[1] - second[1]

            antinode = (first[0] + delta_y, first[1] + delta_x)
            if is_valid(antinode):
                antinodes.add(antinode)

            antinode = (second[0] - delta_y, second[1] - delta_x)
            if is_valid(antinode):
                antinodes.add(antinode)

    return len(antinodes)


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def test_solve():
    assert solve(EXAMPLE) == 14
