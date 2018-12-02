import sys

def compare_ids(id_one, id_two):
    indices = range(len(id_one) - 1)
    different_chars = 0
    for index in indices:
        if id_one[index] != id_two[index]:
            different_chars += 1
    return different_chars

match_one, match_two, common_chars = '', '', ''

with open(sys.argv[1]) as input_file:
    box_ids = list(input_file)
    for box_id_one in box_ids:
        for box_id_two in box_ids:
            if compare_ids(box_id_one, box_id_two) == 1:
                match_one, match_two = box_id_one, box_id_two

for char_one, char_two in zip(match_one, match_two):
    if char_one == char_two:
        common_chars += char_one

print(common_chars)
