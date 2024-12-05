from collections import defaultdict


def solve(input_data):
    answer = 0
    rules, updates = input_data.split("\n\n")

    # Construct rulebook.
    rules = [rule.split("|") for rule in (rule for rule in rules.split("\n"))]
    rulebook = defaultdict(list)
    for rule in rules:
        rulebook[rule[0]].append(rule[1])

    def get_invalid_page_number(pages):
        for i in range(len(pages) - 1):
            pages_to_check = pages[i + 1 :]

            for page_to_check in pages_to_check:
                if page_to_check not in rulebook[pages[i]]:
                    return pages.index(page_to_check)
        return None

    for update in updates.split("\n"):
        pages = update.split(",")

        invalid_page = get_invalid_page_number(pages)

        if invalid_page:
            while invalid_page:
                # Swap page number with previous one.
                pages[invalid_page], pages[invalid_page - 1] = (
                    pages[invalid_page - 1],
                    pages[invalid_page],
                )
                invalid_page = get_invalid_page_number(pages)
            answer += int(pages[int((len(pages) - 1) / 2)])

    return answer


if __name__ == "__main__":
    input_data = open("input.txt").read()
    print(solve(input_data))

EXAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_solve():
    assert solve(EXAMPLE) == 123
