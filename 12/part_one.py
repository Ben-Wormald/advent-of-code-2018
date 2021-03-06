import sys

with open(sys.argv[1]) as input_file:
    input = list(input_file)
    
state = '.' * 24 + input[0].split(' ')[2][:-1] + '.' * 24
conditions = []

for line in input[2:]:
    line_parts = line.split(' ')
    conditions.append({
        'state': line_parts[0],
        'result': line_parts[2][0]
    })

for generation in range(20):
    new_state = state
    for i_state in range(len(state) - 4):
        for condition in conditions:
            if condition['state'] == state[i_state:i_state + 5]:
                new_state = new_state[:i_state + 2] + condition['result'] + new_state[i_state + 3:]

    state = new_state

state_id, id_sum = -24, 0
for char in state:
    if char == '#':
        id_sum += state_id
    state_id += 1

print(id_sum)
