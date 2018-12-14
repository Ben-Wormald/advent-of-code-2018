import sys

input = int(sys.argv[1])

recipes = [3, 7]
elf_one, elf_two = 0, 1

while len(recipes) < input + 10:
    recipe_one, recipe_two = recipes[elf_one], recipes[elf_two]
    new_recipe = recipe_one + recipe_two
    
    recipes = recipes + list(int(digit) for digit in str(new_recipe))

    elf_one = (elf_one + recipe_one + 1) % len(recipes)
    elf_two = (elf_two + recipe_two + 1) % len(recipes)

print(''.join(str(recipe) for recipe in recipes[input:input + 10]))
