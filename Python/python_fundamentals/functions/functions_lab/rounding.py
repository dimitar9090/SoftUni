current_number = input().split(" ")
rounded_numbers = []
for number in current_number:
    rounded_numbers.append(round(float(number)))
print(rounded_numbers)