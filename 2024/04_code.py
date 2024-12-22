from utils import load_file


def parse_input(by: str = None) -> list[str]:
    data = load_file(day=4)
    rows = data.split("\n")
    row_length = len(rows[0])
    if by == "left":
        for i in range(row_length):
            rows[i] = "." * (row_length - i - 1) + rows[i] + "." * i
        return rows
    elif by == "right":
        for i in range(row_length):
            rows[i] = "." * i + rows[i] + "." * (row_length - i - 1)
        return rows
    else:
        return rows


def count_rows(rows: list[str]) -> int:
    result = 0
    for row in rows:
        result += row.count("XMAS")
        result += row.count("SAMX")
    return result


def count_cols(rows: list[str]) -> int:
    result = 0
    for i in range(len(rows[0])):
        col = "".join([row[i] for row in rows])
        result += col.count("XMAS")
        result += col.count("SAMX")
    return result


def part1():
    rows = parse_input()
    left = parse_input(by="left")
    right = parse_input(by="right")
    result = count_rows(rows) + count_cols(rows) + count_cols(left) + count_cols(right)
    print(result)

def part2():
    rows = parse_input()
    result = 0
    for i, row in enumerate(rows[1:-1], start=1):
        for j, letter in enumerate(row[1:-1], start=1):
            if letter != "A":
                continue

            # M to the left
            if rows[i - 1][j - 1] == "M" and rows[i + 1][j + 1] == "S" and rows[i + 1][j - 1] == "M" and rows[i - 1][j + 1] == "S":
                result += 1
            
            # M to the right
            if rows[i - 1][j + 1] == "M" and rows[i + 1][j - 1] == "S" and rows[i + 1][j + 1] == "M" and rows[i - 1][j - 1] == "S":
                result += 1
            
            # M on top
            if rows[i - 1][j - 1] == "M" and rows[i + 1][j + 1] == "S" and rows[i - 1][j + 1] == "M" and rows[i + 1][j - 1] == "S":
                result += 1
            
            # M on bottom
            if rows[i + 1][j - 1] == "M" and rows[i - 1][j + 1] == "S" and rows[i + 1][j + 1] == "M" and rows[i - 1][j - 1] == "S":
                result += 1
    print(result)


if __name__ == "__main__":
    part1()
    part2()
