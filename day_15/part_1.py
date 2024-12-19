def solve(input_data):
    DIRECTIONS = {
        "<": (0, -1),
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
    }

    raw_warehouse, raw_movements = input_data.split("\n\n")

    # Get warehouse and robot data.
    warehouse = {}
    for y, line in enumerate(raw_warehouse.split("\n")):
        for x, char in enumerate(line):
            warehouse[(y, x)] = char
            if char == "@":
                robot = (y, x)

    # Prepare movements.
    movements = "".join(raw_movements.split("\n"))

    # Recursive function to apply robot movement.
    def apply_movement(position, direction):
        position_to_check = (position[0] + direction[0], position[1] + direction[1])
        if warehouse[position_to_check] == ".":
            warehouse[position_to_check] = warehouse[position]
            return True
        elif warehouse[position_to_check] == "#":
            return False
        else:
            result = apply_movement(position_to_check, direction)
            if result:
                warehouse[position_to_check] = warehouse[position]
                return True

    for move in movements:
        direction = DIRECTIONS[move]

        if apply_movement(robot, direction):
            warehouse[robot] = "."
            robot = (robot[0] + direction[0], robot[1] + direction[1])
            warehouse[robot] = "@"

    # Compute answer.
    answer = 0
    for position, value in warehouse.items():
        if value == "O":
            answer += 100 * position[0] + position[1]
    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


def test_solve():
    assert solve(EXAMPLE) == 10092
