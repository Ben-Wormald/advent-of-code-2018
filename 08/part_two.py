import sys

with open(sys.argv[1]) as input_file:
    data = list(input_file)[0][:-1].split(' ')

def build_tree(data, i_data):
    n_children = int(data[i_data])
    i_data += 1
    n_metadata = int(data[i_data])
    i_data += 1

    subtree = {
        'n_children': n_children,
        'n_metadata': n_metadata,
        'children': [],
        'metadata': []
    }

    for i_child in range(n_children):
        child, i_data = build_tree(data, i_data)
        subtree['children'].append(child)

    for i_metadata in range(n_metadata):
        subtree['metadata'].append(int(data[i_data]))
        i_data += 1

    return subtree, i_data

tree, i_data = build_tree(data, 0)

def get_value(subtree):
    if subtree['n_children'] == 0:
        return sum(subtree['metadata'])

    else:
        metadata_sum = 0
        for i_child in subtree['metadata']:
            if i_child <= len(subtree['children']):
                metadata_sum += get_value(subtree['children'][i_child - 1])
        return metadata_sum

metadata_sum = get_value(tree)
print(metadata_sum)
