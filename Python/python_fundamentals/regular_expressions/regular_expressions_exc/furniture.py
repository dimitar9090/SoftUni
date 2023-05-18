import re
items = []
total_price = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
text = input()
while text != "Purchase":
    match = re.search(pattern, text)
    if match:
        furniture, price, quantity = match.groups()
        items.append(furniture)
        total_price += float(price) * int(quantity)
    text = input()
print("Bought furniture:")
if items:
    print("\n".join(items))
print(f"Total money spend: {total_price:.2f}")