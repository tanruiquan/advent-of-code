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


RED = 12
GREEN = 13
BLUE = 14


def is_possible(draws):
    for draw in draws:
        for colour, number in draw.items():
            number = int(number)
            if colour == "red" and number > RED:
                return False

            if colour == "green" and number > GREEN:
                return False

            if colour == "blue" and number > BLUE:
                return False
    return True


def parse_data(data):
    res = defaultdict(list)
    for line in data:
        game, draws = line.split(":")
        _, game_no = game.split()

        draws = draws.split(";")
        for i, draw in enumerate(draws):
            colours = draw.split(",")
            to_add = {}
            for c in colours:
                c = c.strip()
                count, colour = c.split()
                to_add[colour] = count
            res[game_no].append(to_add)
    return res


if __name__ == '__main__':
    data = read_file(file_path)
    games = parse_data(data)
    res = 0
    for game_id, draws in games.items():
        if is_possible(draws):
            res += int(game_id)
    print(res)
