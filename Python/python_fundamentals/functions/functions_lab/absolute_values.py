numbers = input().split(" ")
list_of_abs_numbers = []
for number in numbers:
    list_of_abs_numbers.append(abs(float(number)))
print(list_of_abs_numbers)