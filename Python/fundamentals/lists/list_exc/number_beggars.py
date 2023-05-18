single_string_of_integers = input().split(", ")
number_of_beggars = int(input())
final_sums = []
money_list_digits = []
starting_index = 0
for element in single_string_of_integers:
    money_list_digits.append(int(element))
while starting_index < number_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(starting_index, len(money_list_digits), number_of_beggars):
        sum_of_current_beggar += money_list_digits[current_index]
    final_sums.append(sum_of_current_beggar)
    starting_index += 1
print(final_sums)