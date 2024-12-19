import re
from collections import defaultdict


def solve(input_data):
    robot_re = re.compile(r"^p=(\d+),(\d+) v=(.+),(.+)$")

    WIDTH = 101
    HEIGHT = 103

    robots = []
    for robot in input_data.split("\n"):
        robot_x, robot_y, velocity_x, velocity_y = map(
            int, robot_re.match(robot).groups()
        )
        robots.append((robot_x, robot_y, velocity_x, velocity_y))

    def find_largest_connected_part(numbers):
        numbers = sorted(numbers)
        max_sequence = 0
        current_sequence = 0

        for index in range(len(numbers) - 1):
            if numbers[index] + 1 == numbers[index + 1]:
                current_sequence += 1
            else:
                current_sequence = 1

            if current_sequence > max_sequence:
                max_sequence = current_sequence
        return max_sequence

    seconds = 0
    while True:
        seconds += 1
        verticals = defaultdict(set)
        for index in range(len(robots)):
            robot_x, robot_y, velocity_x, velocity_y = robots[index]

            robot_x = (robot_x + velocity_x) % WIDTH
            robot_y = (robot_y + velocity_y) % HEIGHT

            robots[index] = (robot_x, robot_y, velocity_x, velocity_y)

            verticals[robot_x].add(robot_y)

        if any(find_largest_connected_part(x) > 30 for x in verticals.values()):
            break
    return seconds


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))
