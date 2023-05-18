def minimum(current_numbers):
    return f"The minimum number is {min(map(int,current_numbers))}"


def maximum(current_numbers):
    return f"The maximum number is {max(map(int, current_numbers))}"


def sum_of(current_numbers):
    return f"The sum number is: {sum(map(int,current_numbers))}"


number = input().split(" ")
print(minimum(number))
print(maximum(number))
print(sum_of(number))