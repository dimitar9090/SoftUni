current_strings = input().split(" ")
result = ""
for word in current_strings:
    result += word * len(word)
print(result)