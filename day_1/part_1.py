input_data = open("example.txt").read()

left = []
right = []

for line in input_data.splitlines():
    x, y = map(int, line.split())
    left.append(x)
    right.append(y)

left.sort()
right.sort()

print(sum(abs(x - y) for x, y in zip(left, right, strict=False)))
