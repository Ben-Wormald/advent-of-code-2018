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

initial_steps = int(-0.9999 * points[0]['p_x'] / points[0]['v_x'])

for point in points:
    point['p_x'] += initial_steps * point['v_x']
    point['p_y'] += initial_steps * point['v_y']

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

done = False
prev_range_sum = None
steps = initial_steps - 1

while not done:
    prev_points = copy.deepcopy(points)

    for point in points:
        point['p_x'] += point['v_x']
        point['p_y'] += point['v_y']

    steps += 1

    min_x, max_x, min_y, max_y = get_ranges(points)
    range_sum = max_x - min_x + max_y - min_y

    if prev_range_sum is None or range_sum < prev_range_sum:
        prev_range_sum = range_sum
    else:
        print(steps)
        break
