string = input()
current_list = []
for letter in string:
    current_list.append(letter)
while len(current_list) > 0:
    print(current_list.pop(), end="")