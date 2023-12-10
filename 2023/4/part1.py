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


def calculate_points(card):
    _, numbers = card.split(":")
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()
    points = 0
    for num in my_numbers:
        if num in winning_numbers:
            points += 1
    return 2**(points-1) if points else 0


def solve(cards):
    res = 0
    for card in cards:
        res += calculate_points(card)
    return res


if __name__ == "__main__":
    cards = read_file(file_path)
    print(solve(cards))
