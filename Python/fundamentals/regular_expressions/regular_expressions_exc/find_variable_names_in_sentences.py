import re
text = input()
variables = []
pattern = r"\b_[A-Za-z0-9]+\b"
matches = re.findall(pattern, text)
for match in matches:
    variables.append(match[1:])
print(','.join(variables))