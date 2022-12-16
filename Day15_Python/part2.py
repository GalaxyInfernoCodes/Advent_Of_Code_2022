def manhatten_distance(a_x, a_y, b_x, b_y):
    return abs(a_x - b_x) + abs(a_y - b_y)


def check_field_empty(y_index, x_index, sensors, beacons):
    for sensor in sensors:
        if manhatten_distance(x_index, y_index, sensor[0], sensor[1]) <= sensor[2]:
            return False
    for beacon in beacons:
        if y_index == beacon[1] and x_index == beacon[0]:
            return False
    return True


def traverse_border(sensor_x, sensor_y, distance, max_zone, sensors, beacons):
    if sensor_y - distance < 0:
        half_width = - (sensor_y - distance)
    else: 
        half_width = 0
    #top
    top = sensor_y-distance-1
    if top > 0:
        if check_field_empty(top, sensor_x, sensors, beacons):
            print('omg finally', 'y', top, 'x', sensor_x)
            print('solution', sensor_x * 4000000 + top)
            return True
    #bottom
    bottom = sensor_y+distance+1
    if bottom <= max_zone + 1:
        if check_field_empty(bottom, sensor_x, sensors, beacons):
            print('omg finally', 'y', bottom, 'x', sensor_x)
            print('solution', sensor_x * 4000000 + bottom)
            return True
    #left and right
    for y in range(max(0, sensor_y - distance), min(sensor_y + distance + 1, max_zone+1)):
        # left 
        left = sensor_x - half_width - 1
        if left > 0:
            if check_field_empty(y, left, sensors, beacons):
                print('omg finally', 'y', y, 'x', left)
                print('solution', left * 4000000 + y)
                return True
        right = sensor_x + half_width + 1
        if right <= max_zone+1:
            if check_field_empty(y, right, sensors, beacons):
                print('omg finally', 'y', y, 'x', right)
                print('solution', right * 4000000 + y)
                return True
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1
    return False

def save_no_beacon_zone(grid, sensor_x, sensor_y, distance, y_index):
    if sensor_y - distance < 0:
        half_width = - (sensor_y - distance)
    else:
        half_width = 0
    for y in range(sensor_y - distance, sensor_y + distance + 1):
        if y == y_index:
            for x in range(sensor_x - half_width, sensor_x + half_width + 1):
                grid.add(x)
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1

def solve2(file, max_zone): 
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    sensors = []
    beacons = []
    for i, line in enumerate(lines):
        #print(line)
        parts_with_numbers = [word for word in line.split(' ') if '='in word]
        parts_with_numbers_cleaned = [word.replace(',', '').replace(':', '') for word in parts_with_numbers]
        sensor_x, sensor_y, beacon_x, beacon_y = list(map(lambda x: int(x.split('=')[1]), parts_with_numbers_cleaned))

        distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        
        sensors.append([sensor_x, sensor_y, distance_to_beacon])
        beacons.append([beacon_x, beacon_y])

    for i, sensor in enumerate(sensors):
        print('sensor', i)
        if traverse_border(sensor[0], sensor[1], sensor[2], max_zone, sensors, beacons):
            return
        



if __name__ == "__main__":
    print('example')
    solve2('example.txt', 20)
    print('input')
    solve2('input.txt', 4000000)