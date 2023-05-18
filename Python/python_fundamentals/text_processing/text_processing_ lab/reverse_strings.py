while True:
    current_command = input()
    if current_command == "end":
        break
    print(f"{current_command} = {current_command[::-1]}")
