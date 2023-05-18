def check_if_palindrome(current_numbers):
    for number in current_numbers:
        if int(number) == int(number[::-1]):
            print(True)
        elif int(number) != int(number[::-1]):
            print(False)


numbers = input().split(", ")
check_if_palindrome(numbers)