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

max_x += 1
max_y += 1

grid = [['.'] * max_y for x in range(max_x)]

for point in points:
    grid[point['x']][point['y']] = point['id']

def distanceToPoint(x, y, point):
    return abs(x - point['x']) + abs(y - point['y'])

def closestPoint(x, y, points):
    min_distance, min_point = None, None
    tie = False

    for point in points:
        distance = distanceToPoint(x, y, point)

        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_point = point['id']
            tie = False
        elif distance == min_distance:
            tie = True

    return '.' if tie else min_point

for i_x in range(len(grid)):
    for i_y in range(len(grid[i_x])):

        if grid[i_x][i_y] == '.':
            print(closestPoint(i_x, i_y, points), end='')
        else:
            print(grid[i_x][i_y].upper(), end='')
    print('\n', end='')
