import sys

with open(sys.argv[1]) as input_file:
    data = list(input_file)[0][:-1].split(' ')

nodes = []
state = 'header_children'
metadata_sum = 0
    
for datum in data:
    datum = int(datum)
    
    if state == 'header_children':
        nodes.append({
            'children': datum,
            'metadata': None
        })
        state = 'header_metadata'

    elif state == 'header_metadata':
        nodes[-1]['metadata'] = datum

        if nodes[-1]['children'] > 0:
            state = 'header_children'
        else:
            state = 'metadata'

    elif state == 'metadata':
        metadata_sum += datum

        nodes[-1]['metadata'] += -1
        if nodes[-1]['metadata'] == 0:
            nodes = nodes[:-1]

            if not len(nodes):
                break

            nodes[-1]['children'] += -1
            if nodes[-1]['children'] > 0:
                state = 'header_children'

print(metadata_sum)
