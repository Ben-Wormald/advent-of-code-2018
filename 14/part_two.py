import sys

input = sys.argv[1]
input_digits = list(int(digit) for digit in input)

recipes = [3, 7]
elf_one, elf_two = 0, 1
done = False
matched_input_digit = 0

while not done:
    recipe_one, recipe_two = recipes[elf_one], recipes[elf_two]
    new_recipe = recipe_one + recipe_two
    new_recipe_digits = list(int(digit) for digit in str(new_recipe))

    recipes = recipes + new_recipe_digits

    for digit in new_recipe_digits:
        print(recipes)
        print(digit,input_digits[matched_input_digit])
        if digit == input_digits[matched_input_digit]:
            matched_input_digit += 1
        elif matched_input_digit != 0:
            matched_input_digit = 0
            break

        if matched_input_digit == len(input_digits):
            print(len(recipes[:-len(input_digits)]))
            done = True
            break

    elf_one = (elf_one + recipe_one + 1) % len(recipes)
    elf_two = (elf_two + recipe_two + 1) % len(recipes)

    if len(recipes) > 30:
        break