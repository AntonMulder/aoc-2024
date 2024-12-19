from queue import PriorityQueue


def solve(input_data):
    DIRECTIONS = [
        (0, 1),  # East.
        (1, 0),  # South.
        (0, -1),  # West.
        (-1, 0),  # North.
    ]
    direction = 0  # Start direction is East.
    queue = PriorityQueue()
    visited_with_scores = {}
    lowest_costs = None
    spots = set()

    # Create maze data.
    maze = {}
    for y, line in enumerate(input_data.split("\n")):
        for x in range(len(line)):
            maze[(y, x)] = line[x]

            if line[x] == "S":
                reindeer = (y, x)
                queue.put((0, reindeer, direction, {reindeer}))
                visited_with_scores[reindeer, direction] = 0

    # Find all possible "cheapest" routes.
    while True:
        score, reindeer, direction, visited = queue.get()
        for x in range(4):
            new_direction = (direction + x) % 4
            possible_location = (
                reindeer[0] + DIRECTIONS[new_direction][0],
                reindeer[1] + DIRECTIONS[new_direction][1],
            )

            if maze[possible_location] == "E":
                visited.add(possible_location)

                if not lowest_costs:
                    lowest_costs = score + 1

                if score + 1 == lowest_costs:
                    spots.update(visited)
                else:
                    return len(spots)
            elif possible_location not in visited and maze[possible_location] != "#":
                new_score = score + 1
                if new_direction != direction:
                    new_score += 1000

                new_visited = visited.copy()
                new_visited.add(possible_location)

                if visited_score := visited_with_scores.get(
                    (possible_location, direction), None
                ):
                    if new_score <= visited_score:
                        visited_with_scores[(possible_location, direction)] = new_score
                        queue.put(
                            (new_score, possible_location, new_direction, new_visited)
                        )
                else:
                    visited_with_scores[(possible_location, direction)] = new_score
                    queue.put(
                        (new_score, possible_location, new_direction, new_visited)
                    )


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
    assert solve(EXAMPLE) == 64
