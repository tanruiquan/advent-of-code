from collections import Counter

from utils import load_file


def load_input():
    data = load_file(day=1)
    rows = data.split("\n")
    all_left = []
    all_right = []
    for row in rows:
        left, right = row.split()
        all_left.append(left)
        all_right.append(right)
    return all_left, all_right


def part1():
    all_left, all_right = load_input()
    all_left.sort()
    all_right.sort()
    result = 0
    for left, right in zip(all_left, all_right):
        result += abs(int(left) - int(right))
    print(result)


def part2():
    all_left, all_right = load_input()
    counts = Counter(all_right)
    result = 0
    for num in all_left:
        if num in counts:
            result += int(num) * counts.get(num)
    print(result)


if __name__ == "__main__":
    part1()
    part2()
