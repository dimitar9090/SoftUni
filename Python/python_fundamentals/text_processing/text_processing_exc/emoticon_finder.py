current_string = input()
for index in range(len(current_string)):
    if current_string[index] == ":" and index != len(current_string) - 1:
        print(f":{current_string[index + 1]}")
