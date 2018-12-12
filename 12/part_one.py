import sys

with open(sys.argv[1]) as input_file:
    input = list(input_file)
    
initial_state = input[0].split(' ')[2][:-1]
conditions = []

for line in input[2:]:
    line_parts = line.split(' ')
    conditions.append({
        'state': line_parts[0],
        'result': line_parts[2][0]
    })
