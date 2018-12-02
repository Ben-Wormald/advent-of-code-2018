import sys

def check_id(box_id):
    two, three = 0, 0
    for char in box_id:
        char_count = box_id.count(char)
        if char_count == 2:
            two = 1
        if char_count == 3:
            three = 1
    return two, three

twos, threes = 0, 0

with open(sys.argv[1]) as input_file:
    for box_id in input_file:
        two, three = check_id(box_id)
        twos += two
        threes += three

checksum = twos * threes
print(checksum)
