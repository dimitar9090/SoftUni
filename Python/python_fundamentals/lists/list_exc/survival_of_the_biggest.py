list_of_numbers = input().split()
list_of_integers = []
number_of_numbers = int(input())
for element in list_of_numbers:
    list_of_integers.append(int(element))
for current_number in range(number_of_numbers):
    list_of_integers.remove(min(list_of_integers))
print(*list_of_integers, sep=", ")