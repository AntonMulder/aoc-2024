def solve(input_data):
    # Create initial file structure.
    free_space = False
    id = 0
    memory = []
    for file in input_data:
        if free_space:
            memory.extend(["." for _ in range(int(file))])
            free_space = False
        else:
            memory.extend([id for _ in range(int(file))])
            free_space = True
            id += 1

    def get_first_free_space(memory):
        try:
            return memory.index(".")
        except ValueError:
            return -1

    # Format memory.
    while (first_free_memory_space := get_first_free_space(memory)) != -1:
        while (value := memory.pop()) == ".":
            pass
        memory[first_free_memory_space] = value

    return sum(index * value for index, value in enumerate(memory))


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = "2333133121414131402"


def test_solve():
    assert solve(EXAMPLE) == 1928
