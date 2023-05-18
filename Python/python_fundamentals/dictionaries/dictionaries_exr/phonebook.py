phonebook = {}
while True:
    current_command = input()
    if "-" not in current_command:
        break
    name, phone_number = current_command.split("-")
    phonebook[name] = phone_number
for check in range(int(current_command)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")