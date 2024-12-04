def christmas_counter(temp):
    return temp.count("XMAS") + temp.count("SAMX")


def solve(input_data):
    board = input_data.split("\n")

    answer = 0
    height = len(board)
    width = len(board[0])

    # Horizontal
    answer += sum(christmas_counter(board[i]) for i in range(height))

    # Vertical
    answer += sum(
        christmas_counter(column)
        for column in (
            "".join(board[j][i] for j in range(height)) for i in range(len(board[0]))
        )
    )

    # Diagonal
    for i in range(width):
        for j in (
            x for x, c in enumerate(board[i]) if c in {"X", "S"} and x < width - 3
        ):
            if i < height - 3:
                diagonal = "".join(board[i + x][j + x] for x in range(4))
                answer += christmas_counter(diagonal)
            if i >= 3:
                diagonal = "".join(board[i - x][j + x] for x in range(4))
                answer += christmas_counter(diagonal)

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_solve():
    assert solve(EXAMPLE) == 18
