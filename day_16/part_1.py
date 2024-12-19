from queue import PriorityQueue


def solve(input_data):
    DIRECTIONS = [
        (0, 1),  # East.
        (1, 0),  # South.
        (0, -1),  # West.
        (-1, 0),  # North.
    ]
    direction = 0  # Start direction is East.
    visited = set()
    queue = PriorityQueue()

    # Create maze data.
    maze = {}
    for y, line in enumerate(input_data.split("\n")):
        for x in range(len(line)):
            maze[(y, x)] = line[x]

            if line[x] == "S":
                reindeer = (y, x)
                visited = {(y, x)}
                queue.put((0, reindeer, direction))

    while True:
        score, reindeer, direction = queue.get()
        # Find "cheapest" route.
        for x in range(4):
            new_direction = (direction + x) % 4
            possible_location = (
                reindeer[0] + DIRECTIONS[new_direction][0],
                reindeer[1] + DIRECTIONS[new_direction][1],
            )
            if maze[possible_location] == "E":
                return score + 1
            if possible_location not in visited and maze[possible_location] != "#":
                new_score = score + 1
                if new_direction != direction:
                    new_score += 1000
                queue.put((new_score, possible_location, new_direction))
                visited.add(possible_location)


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def test_solve():
    assert solve(EXAMPLE) == 11048
