input_data = open("example.txt").read()

valid = 0


def is_valid(level):
    if level == sorted(level) or level == sorted(level, reverse=True):
        diff = [abs(y - x) for x, y in zip(level, level[1:])]

        if all(1 <= x <= 3 for x in diff):
            return True
    return False


for line in input_data.splitlines():
    level = list(map(int, line.split()))

    if is_valid(level):
        valid += 1

print(valid)
