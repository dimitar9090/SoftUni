current_text = input()
encrypted_text = " "
for character in current_text:
    ch = ord(character) + 3
    encrypted_text += chr(ch)
print(encrypted_text)