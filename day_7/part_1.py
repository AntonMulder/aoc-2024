def solve(input_data):
    final_answer = 0

    for eq in input_data.split("\n"):
        answer, numbers = eq.split(": ")
        answer = int(answer)
        numbers = numbers.split(" ")

        # Create possible options (Naive).
        options = [[numbers.pop(0)]]
        for number in numbers:
            new_options = []
            for action in ["+", "*"]:
                for option in options:
                    new_options.append(option + [action, number])
            options = new_options

        # Check if one of the options is valid.
        for option in options:
            value = int(option.pop(0))

            while len(option):
                operator = option.pop(0)
                new_value = int(option.pop(0))

                value = value + new_value if operator == "+" else value * new_value

                # Early exit.
                if value > answer:
                    break

            if value == answer:
                final_answer += value
                break

    return final_answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))


EXAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_solve():
    assert solve(EXAMPLE) == 3749
