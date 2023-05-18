number_of_inputs = int(input())
sum_of_characters = 0
for current_character in range(number_of_inputs):
    current_character = input()
    sum_of_characters += ord(current_character)
print(f"The sum equals: {sum_of_characters}")