import sys

input_file = open(sys.argv[1])

freq = 0

for line in input_file:
    freq += int(line)

print(freq)
