def solve(input_data):
    board = input_data.split("\n")

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    # Get starting position
    for y in range(len(board)):
        if (x := board[y].find("^")) != -1:
            position = (y, x)
            break

    # Walk through board.
    visited = set()
    while True:
        visited.add(position)

        position_ahead = (
            position[0] + DIRECTIONS[direction][0],
            position[1] + DIRECTIONS[direction][1],
        )

        if not (
            0 <= position_ahead[0] < len(board)
            and 0 <= position_ahead[1] < len(board[0])
        ):
            break

        if board[position_ahead[0]][position_ahead[1]] == "#":
            # Turn right
            direction = (direction + 1) % 4
        else:
            position = position_ahead

    return len(visited)


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_solve():
    assert solve(EXAMPLE) == 41
