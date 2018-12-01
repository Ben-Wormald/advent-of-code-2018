import sys

input_file = open(sys.argv[1])

freq = 0
found = False
found_freqs = [freq]

while not found:
    for line in input_file:
        freq += int(line)

        if freq in found_freqs:
            found = True
            break

        found_freqs.append(freq)
    input_file.seek(0)

print(freq)
