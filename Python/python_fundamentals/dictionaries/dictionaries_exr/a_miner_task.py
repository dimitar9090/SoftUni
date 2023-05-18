materials = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource not in materials.keys():
        materials[current_resource] = 0
    materials[current_resource] += current_quantity
for resource, quantity in materials.items():
    print(f"{resource} -> {quantity}")