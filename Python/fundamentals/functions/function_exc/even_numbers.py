def list_even_numbers(current_number):

    if int(current_number) % 2 == 0:
        return current_number


numbers = input().split()
even_numbers = list(filter(list_even_numbers, numbers))

print(list(map(int, even_numbers)))
