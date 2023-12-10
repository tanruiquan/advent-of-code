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


def get_power(draws):
    red = 0
    green = 0
    blue = 0
    for draw in draws:
        if "red" in draw:
            red = max(red, int(draw["red"]))
        if "green" in draw:
            green = max(green, int(draw['green']))
        if "blue" in draw:
            blue = max(blue, int(draw["blue"]))
    return red * green * blue


if __name__ == '__main__':
    data = read_file(file_path)
    games = parse_data(data)
    res = 0
    for game_id, draws in games.items():
        res += get_power(draws)
    print(res)
