import sys

logs = []

with open(sys.argv[1]) as input_file:
    for log in input_file:
        for i_log in range(len(logs) + 1):
            log_time = log[1:17]
            minutes_past_midnight = int(log_time.split(':')[1])

            if i_log >= len(logs) or log_time < logs[i_log]['time']:
                logs.insert(i_log, {
                    'time': log_time,
                    'mins': minutes_past_midnight,
                    'type': log[19],
                    'id': log.split(' ')[3][1:] if log[19] == 'G' else None
                })
                break

id_match = False
for i_log in range(len(logs)):
    if logs[i_log]['id'] is not None:
        id_match = logs[i_log]['id'] == '3023'

    if id_match:
        print(logs[i_log])

guards = {}
current_guard, max_guard = None, None
current_max = 0

for i_log in range(len(logs)):
    if logs[i_log]['type'] == 'G':
        current_guard = logs[i_log]['id']
        if current_guard not in guards:
            guards[current_guard] = {
                'mins': [0] * 60,
                'total': 0
            }

    if logs[i_log]['type'] == 'f':
        start_min = logs[i_log]['mins']
        stop_min = logs[i_log + 1]['mins'] - 1

        guards[current_guard]['total'] += stop_min - start_min
        for i_min in range(start_min, stop_min):
            guards[current_guard]['mins'][i_min] += 1

    if guards[current_guard]['total'] > current_max:
        current_max = guards[current_guard]['total']
        max_guard = current_guard

# print(guards)

current_max, max_min = 0, 0

for i_min in range(len(guards[max_guard]['mins'])):
    if guards[max_guard]['mins'][i_min] > current_max:
        current_max = guards[max_guard]['mins'][i_min]
        max_min = i_min

# print(max_min)