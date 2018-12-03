import sys

#1 @ 871,327: 16x20

claims = []
max_x, max_y = 0, 0

with open(sys.argv[1]) as input_file:
    for claim in input_file:
        claim_parts = claim.split(' ')
        pos_parts = claim_parts[2].split(',')
        size_parts = claim_parts[3].split('x')

        claim = {
            'id': int(claim_parts[0][1:]),
            'start': {
                'x': int(pos_parts[0]),
                'y': int(pos_parts[1][:-1]),
            },
            'end': {
                'x': int(size_parts[0]) + int(pos_parts[0]),
                'y': int(size_parts[1]) + int(pos_parts[1][:-1])
            }
        }

        if claim['end']['x'] > max_x:
            max_x = claim['end']['x']
        if claim['end']['y'] > max_y:
            max_y = claim['end']['y']

        claims.append(claim)

fabric = [[0] * max_y for x in range(max_x)]

for claim in claims:
    for x in range(claim['start']['x'], claim['end']['x']):
        for y in range(claim['start']['y'], claim['end']['y']):
            fabric[x][y] += 1

two_plus_claims = 0
for x in range(max_x):
    two_plus_claims += sum(map(lambda value: 1 if value >= 2 else 0, fabric[x]))

print(two_plus_claims)
