import re

from utils import load_file


def mul(num1, num2):
    return num1 * num2


def part1():
    data = load_file(day=3)
    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = pattern.findall(data)
    result = 0

    for match in matches:
        result += eval(match)
    print(result)


def part2():
    data = load_file("data/three.txt")
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    matches = pattern.findall(data)
    result = 0
    can_eval = True
    for match in matches:
        if "do()" in match:
            can_eval = True
        elif "don't()" in match:
            can_eval = False
        elif can_eval:
            result += eval(match)
    print(result)


if __name__ == "__main__":
    part1()
    part2()
