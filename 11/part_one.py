import sys

serial_number = int(sys.argv[1])

GRID_SIZE = 300
grid = [[None] * GRID_SIZE for x in range(GRID_SIZE)]

for i_x in range(GRID_SIZE):
    for i_y in range(GRID_SIZE):
        rack_id = i_x + 10
        power_level = (rack_id * i_y + serial_number) * rack_id
        power_level = int(str(power_level)[-3:-2]) - 5
        grid[i_x][i_y] = power_level

max_power_sum, max_x, max_y = None, None, None

for i_x in range(GRID_SIZE - 2):
    for i_y in range(GRID_SIZE - 2):

        power_sum = 0
        for ii_x in range(i_x, i_x + 3):
            for ii_y in range(i_y, i_y + 3):
                power_sum += grid[ii_x][ii_y]

        if max_power_sum is None or power_sum > max_power_sum:
            max_power_sum = power_sum
            max_x, max_y = i_x, i_y

print(str(max_x) + ',' + str(max_y))
