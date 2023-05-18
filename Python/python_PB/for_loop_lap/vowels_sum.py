word = input()
value = 0
for ch in word:
    if ch == 'a':
        value += 1
    elif ch == 'e':
        value += 2
    elif ch == 'i':
        value += 3
    elif ch == 'o':
        value += 4
    elif ch == 'u':
        value += 5
print(value)


