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


def recover_value(data):
    res = 0
    for line in data:
        line = list(filter(lambda x: x.isnumeric(), line))
        res += int(line[0] + line[-1])
    return res


data = read_file(file_path)
value = recover_value(data)
print(value)
