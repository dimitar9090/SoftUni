command = input()

while command != "End":
    if command != "SoftUni":
        command2 = " "
        for i in command:
            command2 = command2 + i * 2
        print(command2)
    command = input()




