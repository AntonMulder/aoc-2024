from functools import cache


def solve(input_data):
    raw_towel_patterns, designs = input_data.split("\n\n")
    towel_patterns = raw_towel_patterns.split(", ")

    @cache
    def possible_designs(design_to_check):
        if not design_to_check:
            return 1

        designs = 0
        for towel_pattern in towel_patterns:
            if design_to_check.startswith(towel_pattern):
                designs += possible_designs(design_to_check[len(towel_pattern) :])

        return designs

    answer = 0
    for design in designs.split("\n"):
        answer += possible_designs(design)

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_solve():
    assert solve(EXAMPLE) == 16
