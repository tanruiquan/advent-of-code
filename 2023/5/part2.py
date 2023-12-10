from tqdm import tqdm

file_path = "data.txt"


def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file and store them in a list
            lines = file.readlines()
            # Remove any empty lines
            lines = [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    # Initialize variables to store the parsed sections
    seeds = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    # Iterate through the lines and populate the variables
    current_map = None
    for line in lines:
        if line.startswith("seeds:"):
            current_map = seeds
        elif line.startswith("seed-to-soil map:"):
            current_map = seed_to_soil_map
        elif line.startswith("soil-to-fertilizer map:"):
            current_map = soil_to_fertilizer_map
        elif line.startswith("fertilizer-to-water map:"):
            current_map = fertilizer_to_water_map
        elif line.startswith("water-to-light map:"):
            current_map = water_to_light_map
        elif line.startswith("light-to-temperature map:"):
            current_map = light_to_temperature_map
        elif line.startswith("temperature-to-humidity map:"):
            current_map = temperature_to_humidity_map
        elif line.startswith("humidity-to-location map:"):
            current_map = humidity_to_location_map

        # Parse the values from the current line and add them to the current map
        values = [int(value) for value in line.split() if value.isnumeric()]
        if values:
            current_map.append(values)

    # Return the parsed sections as a dictionary
    return {
        "seeds": seeds[0],
        "seed_to_soil_map": seed_to_soil_map,
        "soil_to_fertilizer_map": soil_to_fertilizer_map,
        "fertilizer_to_water_map": fertilizer_to_water_map,
        "water_to_light_map": water_to_light_map,
        "light_to_temperature_map": light_to_temperature_map,
        "temperature_to_humidity_map": temperature_to_humidity_map,
        "humidity_to_location_map": humidity_to_location_map,
    }


def calculate_location(data, seed):
    soil = -1
    for dest, source, length in data["seed_to_soil_map"]:
        if source <= seed < source + length:
            soil = dest + (seed - source)
    if soil == -1:
        soil = seed

    fert = -1
    for dest, source, length in data["soil_to_fertilizer_map"]:
        if source <= soil < source + length:
            fert = dest + (soil - source)
    if fert == -1:
        fert = soil

    water = -1
    for dest, source, length in data["fertilizer_to_water_map"]:
        if source <= fert < source + length:
            water = dest + (fert - source)
    if water == -1:
        water = fert

    light = -1
    for dest, source, length in data["water_to_light_map"]:
        if source <= water < source + length:
            light = dest + (water - source)
    if light == -1:
        light = water

    temp = -1
    for dest, source, length in data["light_to_temperature_map"]:
        if source <= light < source + length:
            temp = dest + (light - source)
    if temp == -1:
        temp = light

    hum = -1
    for dest, source, length in data["temperature_to_humidity_map"]:
        if source <= temp < source + length:
            hum = dest + (temp - source)
    if hum == -1:
        hum = temp

    loc = -1
    for dest, source, length in data["humidity_to_location_map"]:
        if source <= hum < source + length:
            loc = dest + (hum - source)
    if loc == -1:
        loc = hum
    return loc


def solve(data):
    res = None
    for i in tqdm(range(len(data["seeds"])//2), desc="Seeding"):
        i *= 2
        start = data["seeds"][i]
        length = data["seeds"][i+1]
        for j in range(start, start+length):
            if res is None:
                res = calculate_location(data, j)
            else:
                res = min(res, calculate_location(data, j))
    return res


if __name__ == "__main__":
    data = parse_file(file_path)
    print(solve(data))
