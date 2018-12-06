import sys
import string

points = []
max_x, max_y = 0, 0
id_letters = string.ascii_letters

with open(sys.argv[1]) as input_file:
    for line in input_file:
        line_parts = line.split(' ')
        x, y = int(line_parts[0][:-1]), int(line_parts[1][:-1])

        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

        points.append({
            'x': x,
            'y': y,
            'id': id_letters[0]
        })

        id_letters = id_letters[1:]

max_x += 2
max_y += 2

grid = [['.'] * max_y for x in range(max_x)]

for point in points:
    grid[point['x']][point['y']] = point['id']

def distance_to_point(x, y, point):
    return abs(x - point['x']) + abs(y - point['y'])

coords_within_range = 0

for i_x in range(len(grid)):
    for i_y in range(len(grid[i_x])):
        distance_sum = 0

        for point in points:
            distance_sum += distance_to_point(i_x, i_y, point)
        
        if distance_sum < 10000:
            coords_within_range += 1

print(coords_within_range)
