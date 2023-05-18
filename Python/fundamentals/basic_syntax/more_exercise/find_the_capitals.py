single_string = input()
list_of_capital_indexes = []
for index, char in enumerate(single_string):
    if char.isupper():
        list_of_capital_indexes.append(index)
print(list_of_capital_indexes)

