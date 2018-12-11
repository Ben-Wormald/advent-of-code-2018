import sys
import numpy

serial_number = int(sys.argv[1])

GRID_SIZE = 300
grid = numpy.zeros((GRID_SIZE, GRID_SIZE))

for i_x in range(GRID_SIZE):
    for i_y in range(GRID_SIZE):
        rack_id = i_x + 10
        power_level = (rack_id * i_y + serial_number) * rack_id
        power_level = int(str(power_level)[-3:-2]) - 5
        grid[i_x][i_y] = power_level

max_power_sum, max_x, max_y, max_size = None, None, None, None

for size in range(1, GRID_SIZE + 1):
    for i_x in range(GRID_SIZE - (size - 1)):
        for i_y in range(GRID_SIZE - (size - 1)):
            power_sum = grid[i_x:i_x + size, i_y:i_y + size].sum()

            if max_power_sum is None or power_sum > max_power_sum:
                max_power_sum = power_sum
                max_x, max_y = i_x, i_y
                max_size = size

print(str(max_x) + ',' + str(max_y) + ',' + str(max_size))
