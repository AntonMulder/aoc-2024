import re
from functools import reduce
from operator import mul


def solve(input_data):
    robot_re = re.compile(r"^p=(\d+),(\d+) v=(.+),(.+)$")

    WIDTH = 101
    HEIGHT = 103
    SECONDS = 100

    quadrants = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0,
    }
    for robot in input_data.split("\n"):
        robot_x, robot_y, velocity_x, velocity_y = map(
            int, robot_re.match(robot).groups()
        )

        robot_x = (robot_x + velocity_x * SECONDS) % WIDTH
        robot_y = (robot_y + velocity_y * SECONDS) % HEIGHT

        if robot_x < (WIDTH // 2):
            if robot_y < (HEIGHT // 2):
                quadrants["top_left"] += 1
            if robot_y > (HEIGHT // 2):
                quadrants["bottom_left"] += 1
        elif robot_x > (WIDTH // 2):
            if robot_y < (HEIGHT // 2):
                quadrants["top_right"] += 1
            if robot_y > (HEIGHT // 2):
                quadrants["bottom_right"] += 1

    return reduce(mul, quadrants.values())


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def test_solve():
    assert solve(EXAMPLE) == 21
