n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
my_list = []
filtered_list = []
for _ in range(n):
    current_number = int(input())
    my_list.append(current_number)
command = input()
for number in my_list:
    filter_pass = (
            (command == COMMAND_EVEN and number % 2 == 0) or \
            (COMMAND_ODD == command and number % 2 != 0) or \
            (COMMAND_POSITIVE == command and number >= 0) or \
            (COMMAND_NEGATIVE == command and number < 0)
    )
    if filter_pass:
        filtered_list.append(number)
print(filtered_list)
