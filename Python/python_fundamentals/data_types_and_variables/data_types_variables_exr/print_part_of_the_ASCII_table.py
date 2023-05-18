start_character = int(input())
last_character = int(input())
for current_character in range(start_character, last_character + 1):
    print(chr(current_character), end=" ")