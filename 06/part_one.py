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

def closest_point(x, y, points):
    min_distance, min_point = None, None
    tie = False

    for point in points:
        distance = distance_to_point(x, y, point)

        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_point = point['id']
            tie = False
        elif distance == min_distance:
            tie = True

    return '.' if tie else min_point

def outer_ids(grid):
    found_ids = set()

    for i_x in range(len(grid)):
        for i_y in range(len(grid[i_x])):
            if i_x == 0 or i_x == len(grid) - 1 or i_y == 0 or i_y == len(grid[i_x]) - 1:
                found_ids.add(grid[i_x][i_y])

    return found_ids

for i_x in range(len(grid)):
    for i_y in range(len(grid[i_x])):

        if grid[i_x][i_y] == '.':
            grid[i_x][i_y] = closest_point(i_x, i_y, points)

infinite_ids = outer_ids(grid)

closet_point_counts = {}

for i_x in range(len(grid)):
    for i_y in range(len(grid[i_x])):
        if grid[i_x][i_y] not in infinite_ids:

            if grid[i_x][i_y] not in closet_point_counts:
                closet_point_counts[grid[i_x][i_y]] = 1
            else:
                closet_point_counts[grid[i_x][i_y]] += 1

max_id, max_count = None, 0

for point_id in closet_point_counts:
    if closet_point_counts[point_id] > max_count:
        max_id = point_id
        max_count = closet_point_counts[point_id]

print(max_id,  max_count)
