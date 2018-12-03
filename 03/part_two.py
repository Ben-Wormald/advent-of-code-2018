import sys

#1 @ 871,327: 16x20

claims = []
valid_claims = []
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
        valid_claims.append(claim['id'])

fabric = [[None] * max_y for x in range(max_x)]

for claim in claims:
    for x in range(claim['start']['x'], claim['end']['x']):
        for y in range(claim['start']['y'], claim['end']['y']):
            if fabric[x][y] is None:
                fabric[x][y] = claim['id']
            else:
                if fabric[x][y] in valid_claims:
                    valid_claims.remove(fabric[x][y])
                if claim['id'] in valid_claims:
                    valid_claims.remove(claim['id'])

print(valid_claims)
