import re
names = input()
pattern = r'\b[A-Z][a-z]+\s\b[A-Z][a-z]+\b'
matches = re.findall(pattern, names)
print(' '.join(matches))