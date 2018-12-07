import sys
import string

BASE_TIME = 60
WORKER_COUNT = 5

steps, step_ids = [], set()

with open(sys.argv[1]) as input_file:
    for line in input_file:
        line_parts = line.split(' ')
        step_ids.add(line_parts[1])
        step_ids.add(line_parts[7])

    step_ids = sorted(step_ids)

    for step_id in step_ids:
        steps.append({
            'id': step_id,
            'reqs': set(),
            'state': 'waiting',
            'work_time': BASE_TIME + string.ascii_uppercase.index(step_id) + 1,
            'start_time': None
        })

    input_file.seek(0)

    for line in input_file:
        line_parts = line.split(' ')
        for step in steps:
            if step['id'] == line_parts[7]:
                step['reqs'].add(line_parts[1])

completed = set()
available_workers = WORKER_COUNT
current_time = 0

while len(completed) < len(steps):
    for step in steps:
        if step['state'] == 'started' and current_time >= step['start_time'] + step['work_time']:
            step['state'] = 'done'
            completed.add(step['id'])
            available_workers += 1

    for step in steps:
        if step['state'] == 'waiting' and step['reqs'].issubset(completed) and available_workers > 0:
            step['state'] = 'started'
            step['start_time'] = current_time
            available_workers += -1

    current_time += 1

print(current_time - 1)
