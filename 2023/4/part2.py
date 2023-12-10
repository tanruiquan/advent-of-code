from collections import defaultdict


file_path = "data.txt"


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file and store them in a list
            lines = file.readlines()
            # Optional: Strip newline characters from each line
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def calculate_copies(card):
    card_no, numbers = card.split(":")
    card_no = int(card_no.split()[1])

    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()
    points = 0
    for num in my_numbers:
        if num in winning_numbers:
            points += 1

    res = []
    for i in range(points):
        res.append(card_no + i + 1)
    return res


def solve(cards):
    res = defaultdict(int)
    for idx, card in enumerate(cards):
        res[idx+1] += 1
        copies = calculate_copies(card)
        for copy in copies:
            res[copy] += 1 * res[idx+1]
    return sum(res.values())


if __name__ == "__main__":
    cards = read_file(file_path)
    print(solve(cards))
