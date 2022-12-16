def save_no_beacon_zone(grid, sensor_x, sensor_y, distance, y_index):
    half_width = 0
    for y in range(sensor_y - distance, sensor_y + distance + 1):
        if y == y_index:
            for x in range(sensor_x - half_width, sensor_x + half_width + 1):
                grid.add(x)
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1

def solve1(file, y_index): 
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    line_overlaps = set()
    device_line_overlaps = set()

    for i, line in enumerate(lines):
        #print(line)
        parts_with_numbers = [word for word in line.split(' ') if '='in word]
        parts_with_numbers_cleaned = [word.replace(',', '').replace(':', '') for word in parts_with_numbers]
        sensor_x, sensor_y, beacon_x, beacon_y = list(map(lambda x: int(x.split('=')[1]), parts_with_numbers_cleaned))

        if sensor_y == y_index:
            device_line_overlaps.add(sensor_x)
        if beacon_y == y_index:
            device_line_overlaps.add(beacon_x)

        distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if y_index in range(sensor_y - distance_to_beacon, sensor_y + distance_to_beacon):
            save_no_beacon_zone(line_overlaps, sensor_x, sensor_y, distance_to_beacon, y_index)
    print(len(line_overlaps - device_line_overlaps))


if __name__ == "__main__":
    print('example')
    solve1('example.txt', 10)
    print('input')
    solve1('input.txt', 2000000)