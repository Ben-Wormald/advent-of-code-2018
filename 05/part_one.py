import sys

def check_pair(char_a, char_b):
    if char_a.islower() and char_b.isupper() and char_a == char_b.lower():
        return True
    elif char_a.isupper() and char_b.islower() and char_a == char_b.upper():
        return True
    else:
        return False

with open(sys.argv[1]) as input_file:
    chars = list(list(input_file)[0])[:-1]

i_char = 0

while i_char < len(chars) - 1:
    if check_pair(chars[i_char], chars[i_char + 1]):
        del chars[i_char:i_char + 2]
        if i_char > 0:
            i_char += -1
    else:
        i_char += 1

print(len(chars))
