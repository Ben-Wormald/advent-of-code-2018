import sys

with open(sys.argv[1]) as input_file:
    input = list(input_file)
    
state = '.' * 4 + input[0].split(' ')[2][:-1] + '.' * 4
conditions = []

for line in input[2:]:
    line_parts = line.split(' ')
    conditions.append({
        'state': line_parts[0],
        'result': line_parts[2][0]
    })

generations = 0
stable = False
first_index = -4

while not stable:
    new_state = state
    for i_state in range(len(state) - 4):
        for condition in conditions:
            if condition['state'] == state[i_state:i_state + 5]:
                new_state = new_state[:i_state + 2] + condition['result'] + new_state[i_state + 3:]

    if new_state[1:] == state[:-1]:
        stable = True

    if new_state[-3:].count('#'):
        new_state = new_state + '.'
    if new_state[:3].count('#'):
        new_state = '.' + new_state
        first_index += -1

    state = new_state
    generations += 1

state_id, id_sum = first_index, 0
for char in state:
    if char == '#':
        id_sum += state_id + (50000000000 - generations)
    state_id += 1

print(id_sum)
