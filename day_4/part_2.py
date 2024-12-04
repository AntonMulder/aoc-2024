def solve(input_data):
    board = input_data.split("\n")

    answer = 0
    width = len(board)
    for i in range(width - 2):
        for j in (
            x for x, c in enumerate(board[i]) if c in {"M", "S"} and x < width - 2
        ):
            first = "".join(board[i + x][j + x] for x in range(3))
            second = board[i][j + 2] + board[i + 1][j + 1] + board[i + 2][j]

            if (first == "MAS" or first == "SAM") and (
                second == "MAS" or second == "SAM"
            ):
                answer += 1

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
    assert solve(EXAMPLE) == 9
