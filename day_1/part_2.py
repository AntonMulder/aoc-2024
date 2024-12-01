from collections import defaultdict

input_data = open("example.txt").read()

left = []
right = defaultdict(lambda: 0)

for line in input_data.splitlines():
    x, y = map(int, line.split())
    left.append(x)
    right[y] += 1

print(sum(x * right[x] for x in left))
