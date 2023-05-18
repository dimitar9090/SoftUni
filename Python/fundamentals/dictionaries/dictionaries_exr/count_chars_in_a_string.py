my_dictionary = {}
my_input = input()
for char in my_input:
    if char == " ":
        continue
    if char not in my_dictionary:
        my_dictionary[char] = 0
    my_dictionary[char] += 1
for key, value in my_dictionary.items():
    print(f"{key} -> {value}")
