import re


def costs_to_win(a_x, a_y, b_x, b_y, prize_x, prize_y):
    # Normalize equations.
    normalize_y = a_y
    normalize_x = a_x

    # For x.
    normalized_b_x = b_x * normalize_y
    normalized_prize_x = prize_x * normalize_y

    # For y.
    normalized_b_y = b_y * normalize_x
    normalized_prize_y = prize_y * normalize_x

    # Compute number of times b is pressed.
    difference_b = abs(normalized_b_x - normalized_b_y)
    difference_prize = abs(normalized_prize_x - normalized_prize_y)
    b = difference_prize / difference_b
    if not b.is_integer():
        return 0

    # Compute the number of times a is pressed.
    a = (prize_x - b_x * b) / a_x
    if a.is_integer():
        return int(a * 3 + b)
    else:
        return 0


def solve(input_data):
    claw_machines = input_data.split("\n\n")

    answer = 0
    for claw_machine in claw_machines:
        button_a, button_b, prize = claw_machine.split("\n")

        button_re = re.compile(r"^Button [AB]: X\+(\d+), Y\+(\d+)$")
        a_x, a_y = map(int, button_re.match(button_a).groups())
        b_x, b_y = map(int, button_re.match(button_b).groups())

        prize_re = re.compile(r"^Prize: X=(\d+), Y=(\d+)$")
        prize_x, prize_y = map(int, prize_re.match(prize).groups())

        answer += costs_to_win(a_x, a_y, b_x, b_y, prize_x, prize_y)
    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_solve():
    assert solve(EXAMPLE) == 480
