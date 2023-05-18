def calculate_num(operator, number_1, number_2):
    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        return round(number_1 / number_2)
    elif operator == "add":
        return number_1 + number_2
    elif operator == "subtract":
        return number_1 - number_2


current_operator = input()
current_number_1 = int(input())
current_number_2 = int(input())
print(calculate_num(current_operator, current_number_1, current_number_2))