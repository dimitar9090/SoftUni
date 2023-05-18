constant_number = int(input())
current_number = 0
while True:
    number = int(input())
    current_number += number
    if current_number >= constant_number:
        print(current_number)
        break