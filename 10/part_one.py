import sys
import copy

points = []

with open(sys.argv[1]) as input_file:
    for line in input_file:
        points.append({
            'p_x': int(line[10:16]),
            'p_y': int(line[18:24]),
            'v_x': int(line[36:38]),
            'v_y': int(line[40:42])
        })

initial_step = int(-0.9999 * points[0]['p_x'] / points[0]['v_x'])

for point in points:
    point['p_x'] += initial_step * point['v_x']
    point['p_y'] += initial_step * point['v_y']

def get_ranges(points):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for point in points:
        if point['p_x'] < min_x:
            min_x = point['p_x']
        elif point['p_x'] > max_x:
            max_x = point['p_x']
        if point['p_y'] < min_y:
            min_y = point['p_y']
        elif point['p_y'] > max_y:
            max_y = point['p_y']

    return min_x, max_x, min_y, max_y

def print_grid(points):
    min_x, max_x, min_y, max_y = get_ranges(points)
    grid = [['.'] * (max_x - min_x + 1) for x in range(max_y - min_y + 1)]

    for point in points:
        grid[point['p_y'] - min_y][point['p_x'] - min_x] = '#'

    for x in grid:
        for y in x:
            print(y, end='')
        print('\n', end='')
    print('\n', end='')

done = False
prev_range_sum = None

while not done:
    prev_points = copy.deepcopy(points)

    for point in points:
        point['p_x'] += point['v_x']
        point['p_y'] += point['v_y']

    min_x, max_x, min_y, max_y = get_ranges(points)
    range_sum = max_x - min_x + max_y - min_y

    if prev_range_sum is None or range_sum < prev_range_sum:
        prev_range_sum = range_sum
    else:
        print_grid(prev_points)
        break
