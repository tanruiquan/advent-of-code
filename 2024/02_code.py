from utils import load_file


def parse_input():
    data = load_file(day=2)
    rows = data.split("\n")
    result = [[int(item) for item in row.split()] for row in rows]
    return result


def is_safely_increasing(row: list[int]) -> bool:
    for i in range(len(row) - 1):
        if row[i + 1] <= row[i] or row[i + 1] - row[i] > 3:
            return False
    return True


def is_safely_decreasing(row: list[int]) -> bool:
    for i in range(len(row) - 1):
        if row[i + 1] >= row[i] or row[i] - row[i + 1] > 3:
            return False
    return True


def part1():
    data = parse_input()
    result = 0
    for i, row in enumerate(data):
        if is_safely_increasing(row) or is_safely_decreasing(row):
            result += 1
    print(result)


def safely_increasing(row: list[int]) -> bool:
    if is_safely_increasing(row[1:]):
        return True
    if is_safely_increasing([row[0]] + row[2:]):
        return True

    prev = row[0]
    flag = True
    for i in range(1, len(row)):
        curr = row[i]
        if curr <= prev:
            if flag:
                flag = False
                continue
            return False
        if curr - prev > 3:
            if flag:
                flag = False
                continue
            return False
        prev = row[i]
    return True


def safely_decreasing(row: list[int]) -> bool:
    if is_safely_decreasing(row[1:]):
        return True
    if is_safely_decreasing([row[0]] + row[2:]):
        return True

    prev = row[0]
    flag = True
    for i in range(1, len(row)):
        curr = row[i]
        if curr >= prev:
            if flag:
                flag = False
                continue
            return False
        if prev - curr > 3:
            if flag:
                flag = False
                continue
            return False
        prev = row[i]
    return True


def part2():
    data = parse_input()
    result = 0
    for i, row in enumerate(data, start=1):
        if safely_increasing(row) or safely_decreasing(row):
            result += 1
    print(result)


if __name__ == "__main__":
    part1()
    part2()
