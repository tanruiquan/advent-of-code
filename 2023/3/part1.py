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


def get_symbols(data):
    symbols = set()
    for line in data:
        for char in line:
            if char.isnumeric() or char == ".":
                continue

            symbols.add(char)
    return symbols


def solve(data, symbols):
    curr = ""
    res = 0
    for i, row in enumerate(data):
        left = 0
        for j, value in enumerate(row):
            if not curr and value.isnumeric():
                left = j
                curr += value
            elif value.isnumeric():
                curr += value
            elif curr and not value.isnumeric():
                if is_part_number(data, i, left, j-1, symbols):
                    res += int(curr)

                # Reset
                curr = ""
                left = 0
        if curr and is_part_number(data, i, left, len(row), symbols):
            res += int(curr)
        curr = ""
        left = 0
    return res


def is_part_number(data, row, left, right, symbols):
    # Check left
    try:
        if data[row][left-1] in symbols:
            return True
    except:
        pass

    # Check right
    try:
        if data[row][right+1] in symbols:
            return True
    except:
        pass

    # Check top
    for i in range(left-1, right+2):
        try:
            if data[row-1][i] in symbols:
                return True
        except:
            pass

    # Check bottom
    for i in range(left-1, right+2):
        try:
            if data[row+1][i] in symbols:
                return True
        except:
            pass

    return False


if __name__ == "__main__":
    data = read_file(file_path)
    symbols = get_symbols(data)
    print(solve(data, symbols))
