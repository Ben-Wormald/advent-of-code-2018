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
                    'id': int(log.split(' ')[3][1:]) if log[19] == 'G' else None
                })
                break

guards = {}
current_guard, max_guard = None, None
max_total = 0

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
        stop_min = logs[i_log + 1]['mins']

        guards[current_guard]['total'] += stop_min - start_min
        for minute in range(start_min, stop_min):
            guards[current_guard]['mins'][minute] += 1

    if guards[current_guard]['total'] > max_total:
        max_total = guards[current_guard]['total']
        max_guard = current_guard

max_guard = None
max_min_count, max_minute = 0, 0

for guard in guards:
    for minute in range(len(guards[guard]['mins'])):
        if guards[guard]['mins'][minute] > max_min_count:
            max_guard = guard
            max_min_count = guards[guard]['mins'][minute]
            max_minute = minute

print(max_guard * max_minute)
