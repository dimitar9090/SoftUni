elements = input().split(" ")
bakary = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakary[key] = int(value)
print(bakary)