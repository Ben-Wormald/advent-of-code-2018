import sys

def check_pair(char_a, char_b):
    if char_a.islower() and char_b.isupper() and char_a == char_b.lower():
        return True
    elif char_a.isupper() and char_b.islower() and char_a == char_b.upper():
        return True
    else:
        return False

with open(sys.argv[1]) as input_file:
    input_str = list(input_file)[0][:-1]
    chars = list(input_str)
    unique_chars = set(list(input_str.lower()))

best_char_value, best_char = None, None

for char in unique_chars:
    i_char = 0
    chars_copy = chars.copy()

    while i_char < len(chars_copy) - 1:
        if chars_copy[i_char].lower() == char:
            del chars_copy[i_char]
        else:
            i_char += 1

    i_char = 0

    while i_char < len(chars_copy) - 1:
        if check_pair(chars_copy[i_char], chars_copy[i_char + 1]):
            del chars_copy[i_char:i_char + 2]
            if i_char > 0:
                i_char += -1
        else:
            i_char += 1

    if best_char_value is None or len(chars_copy) < best_char_value:
        best_char_value = len(chars_copy)
        best_char = char

print(best_char, best_char_value)
