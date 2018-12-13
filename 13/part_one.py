import sys

grid, carts = [], []

with open(sys.argv[1]) as input_file:
    for line in input_file:
        row = []
        for char in line[:-1]:
            if char == '>' or char == '<':
                carts.append({
                    'x': len(grid),
                    'y': len(row)
                })
                char = '-'
            elif char == '^' or char == 'v':
                carts.append({
                    'x': len(grid),
                    'y': len(row)
                })
                char = '|'
                
            row.append(char)
        grid.append(row)

print(grid)
print(carts)
