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


def get_gear_coordinates(data):
    res = {}
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value != "*":
                continue

            count = 0
            temp = []

            # Check left
            if data[i][j-1].isnumeric():
                count += 1
                temp.append((i, j-1))

            # Check right
            if data[i][j+1].isnumeric():
                count += 1
                temp.append((i, j+1))

            # Check top
            if data[i-1][j].isnumeric():
                count += 1
                temp.append((i-1, j))
            else:
                if data[i-1][j-1].isnumeric():
                    count += 1
                    temp.append((i-1, j-1))
                if data[i-1][j+1].isnumeric():
                    count += 1
                    temp.append((i-1, j+1))

            # Check bottom
            if data[i+1][j].isnumeric():
                count += 1
                temp.append((i+1, j))
            else:
                if data[i+1][j-1].isnumeric():
                    count += 1
                    temp.append((i+1, j-1))
                if data[i+1][j+1].isnumeric():
                    count += 1
                    temp.append((i+1, j+1))

            if count == 2:
                res[(i, j)] = temp
    return res


def get_part_number(data, coordinate):
    x, y = coordinate
    res = data[x][y]
    left = y - 1
    right = y + 1

    for i in range(right, len(data[0])):
        if data[x][i].isnumeric():
            res += data[x][i]
        else:
            break

    for i in range(left, -1, -1):
        if data[x][i].isnumeric():
            res = data[x][i] + res
        else:
            break
    return res


def solve(data, coordinates):
    res = 0
    for gear, numbers in coordinates.items():
        num1 = numbers[0]
        num2 = numbers[1]
        res += int(get_part_number(data, num1)) * int(get_part_number(data, num2))
    return res


if __name__ == "__main__":
    data = read_file(file_path)
    gears = get_gear_coordinates(data)
    print(solve(data, gears))
