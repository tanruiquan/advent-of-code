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


def convert_letters(data):
    mapping = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r",
               "five": "f5e", "six": "s6x", "seven": "s7n", "nine": "n9e", "eight": "e8t"}
    res = []
    for line in data:
        for key, value in mapping.items():
            line = line.replace(key, value)
        res.append(line)
    return res


def recover_value(data):
    res = 0
    for line in data:
        line = list(filter(lambda x: x.isnumeric(), line))
        res += int(line[0] + line[-1])
    return res


data = read_file(file_path)
data = convert_letters(data)
value = recover_value(data)
print(value)
