import sys
import copy

grid, carts = [], []

with open(sys.argv[1]) as input_file:
    for line in input_file:
        row = []
        for char in line[:-1]:
            if char == '>' or char == '<':
                carts.append({
                    'id': len(carts),
                    'dir': char,
                    'x': len(row),
                    'y': len(grid),
                    'turn': 'l',
                    'collision': False
                })
                char = '-'
            elif char == 'v' or char == '^':
                carts.append({
                    'id': len(carts),
                    'dir': char,
                    'x': len(row),
                    'y': len(grid),
                    'turn': 'l',
                    'collision': False
                })
                char = '|'
                
            row.append(char)
        grid.append(row)

def move_cart(cart):
    if cart['dir'] == '>':
        cart['x'] += 1
    elif cart['dir'] == '<':
        cart['x'] += -1
    elif cart['dir'] == 'v':
        cart['y'] += 1
    elif cart['dir'] == '^':
        cart['y'] += -1

def turn_left(cart):
    if cart['dir'] == '^':
        cart['dir'] = '<'
    elif cart['dir'] == '<':
        cart['dir'] = 'v'
    elif cart['dir'] == 'v':
        cart['dir'] = '>'
    elif cart['dir'] == '>':
        cart['dir'] = '^'

def turn_right(cart):
    if cart['dir'] == '^':
        cart['dir'] = '>'
    elif cart['dir'] == '>':
        cart['dir'] = 'v'
    elif cart['dir'] == 'v':
        cart['dir'] = '<'
    elif cart['dir'] == '<':
        cart['dir'] = '^'

def turn_cart(cart, grid):
    track = grid[cart['y']][cart['x']]
    direction = cart['dir']

    if track == '/':
        if direction == '>' or direction == '<':
            turn_left(cart)
        else:
            turn_right(cart)
    elif track == '\\':
        if direction == '^' or direction == 'v':
            turn_left(cart)
        else:
            turn_right(cart)
    elif track == '+':
        if cart['turn'] == 'l':
            turn_left(cart)
            cart['turn'] = 's'
        elif cart['turn'] == 's':
            cart['turn'] = 'r'
        elif cart['turn'] == 'r':
            turn_right(cart)
            cart['turn'] = 'l'

while True:
    carts.sort(key=lambda cart: (cart['y'], cart['x']))
    for cart in carts:
        if cart['collision']:
            continue

        move_cart(cart)
        turn_cart(cart, grid)

        for other_cart in carts:
            if other_cart['collision'] or cart['id'] == other_cart['id']:
                continue

            if cart['x'] == other_cart['x'] and cart['y'] == other_cart['y']:
                    cart['collision'] = True
                    other_cart['collision'] = True
                    break
                    
    if sum(1 for cart in carts if not cart['collision']) == 1:
        for cart in carts:
            if not cart['collision']:
                print(str(cart['x']) + ',' + str(cart['y']))
        break
