import sys

steps, step_ids = [], set()

with open(sys.argv[1]) as input_file:
    for line in input_file:
        line_parts = line.split(' ')

        steps.append({
            'id': line_parts[7],
            'req': line_parts[1]
        })
        step_ids.add(line_parts[1])
        step_ids.add(line_parts[7])

step_ids = sorted(step_ids)
completed = []

def get_next_step(steps, completed):
    for step_id in step_ids:
        if step_id not in completed:
            ready = True

            for step in steps:
                if step['id'] == step_id and step['req'] not in completed:
                    ready = False

            if ready:
                return step_id

step_sequence = ''

while len(completed) < len(step_ids):
    next_step = get_next_step(steps, completed)
    step_sequence += next_step
    completed.append(next_step)

print(step_sequence)
