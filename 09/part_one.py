import sys

with open(sys.argv[1]) as input_file:
    input_parts = list(input_file)[0].split(' ')
    n_players = int(input_parts[0])
    last_marble = int(input_parts[6])

circle = [0]
index, current_player = 0, 0
scores = [0] * n_players

for marble in range(1, last_marble):
    if marble % 23 == 0:
        scores[current_player] += marble

        index = (index - 7) % len(circle)
        scores[current_player] += circle[index]
        del circle[index]
        index = index % len(circle)

    else:
        index = (index + 2) % len(circle)
        circle.insert(index, marble)

    current_player = (current_player + 1) % n_players
    
print(max(scores))
