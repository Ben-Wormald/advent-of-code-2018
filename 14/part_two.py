import sys

input = sys.argv[1]
input_digits = list(int(digit) for digit in input)
input_length = len(input_digits)

recipes = [3, 7]
elf_one, elf_two = 0, 1

while True:
    recipe_one, recipe_two = recipes[elf_one], recipes[elf_two]
    new_recipe = recipe_one + recipe_two
    new_recipe_digits = list(int(digit) for digit in str(new_recipe))

    recipes.extend(new_recipe_digits)

    if recipes[-input_length:] == input_digits:
        print(len(recipes[:-input_length]))
        break
    elif recipes[-input_length - 1:-1] == input_digits:
        print(len(recipes[:-input_length - 1]))
        break

    elf_one = (elf_one + recipe_one + 1) % len(recipes)
    elf_two = (elf_two + recipe_two + 1) % len(recipes)
