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
                    'turn': 'l'
                })
                char = '-'
            elif char == 'v' or char == '^':
                carts.append({
                    'id': len(carts),
                    'dir': char,
                    'x': len(row),
                    'y': len(grid),
                    'turn': 'l'
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

collision = False

while not collision:
    carts.sort(key=lambda cart: (cart['y'], cart['x']))
    for cart in carts:
        move_cart(cart)
        turn_cart(cart, grid)

        for other_cart in carts:
            if cart['id'] != other_cart['id'] and cart['x'] == other_cart['x'] and cart['y'] == other_cart['y']:
                print(str(cart['x']) + ',' + str(cart['y']))
                collision = True
                break
            
        if collision:
            break
