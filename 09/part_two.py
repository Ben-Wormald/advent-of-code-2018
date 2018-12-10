import sys
from pyllist import dllist

with open(sys.argv[1]) as input_file:
    input_parts = list(input_file)[0].split(' ')
    n_players = int(input_parts[0])
    last_marble = int(input_parts[6]) * 100

circle = dllist([0])
current_player = 0
scores = [0] * n_players
current_node = circle.first

for marble in range(1, last_marble + 1):
    if marble % 23 == 0:
        scores[current_player] += marble

        for i in range(7):
            current_node = current_node.prev
            if current_node is None:
                current_node = circle.last

        scores[current_player] += current_node.value

        new_current_node = current_node.next
        circle.remove(current_node)
        current_node = new_current_node

    else:
        for i in range(2):
            current_node = current_node.next
            if current_node is None:
                current_node = circle.first

        current_node = circle.insert(marble, current_node)

    current_player = (current_player + 1) % n_players
    
print(max(scores))
