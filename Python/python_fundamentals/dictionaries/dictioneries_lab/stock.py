elements = input().split(" ")
bakary = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakary[key] = int(value)
searching_element = input().split(" ")
for element in searching_element:
    if element in bakary:
        print(f"We have {bakary[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")