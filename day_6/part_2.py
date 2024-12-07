def solve(input_data):
    answer = 0
    board = input_data.split("\n")

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Get starting position
    for y in range(len(board)):
        if (x := board[y].find("^")) != -1:
            start_position = (y, x)
            break

    # Walk through board.
    for obstacle_y in range(len(board)):
        for obstacle_x in range(len(board[0])):
            position = start_position
            direction = 0
            visited = set()
            while True:
                if ((position, position), direction) in visited:
                    answer += 1
                    break
                visited.add(((position, position), direction))

                position_ahead = (
                    position[0] + DIRECTIONS[direction][0],
                    position[1] + DIRECTIONS[direction][1],
                )

                if (
                    position_ahead[0] < 0
                    or position_ahead[0] >= len(board)
                    or position_ahead[1] < 0
                    or position_ahead[1] >= len(board[0])
                ):
                    break

                if board[position_ahead[0]][position_ahead[1]] == "#" or (
                    position_ahead == (obstacle_y, obstacle_x)
                ):
                    # Turn right
                    direction = (direction + 1) % 4
                else:
                    position = position_ahead

    return answer


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
    assert solve(EXAMPLE) == 6
