from collections import deque

textiles = deque(map(int, input().split()))
medical_staff = list(map(int, input().split()))
created_items = {}
while textiles and medical_staff:
    textile = textiles[0]
    medicament = medical_staff[-1]
    total_sum = textile + medicament
    if total_sum in [30, 40, 100]:
        item_table = {30: 'Patch', 40: 'Bandage', 100: 'MedKit'}[total_sum]
        created_items[item_table] = created_items.get(item_table, 0) + 1
        textiles.popleft()
        medical_staff.pop()
    elif total_sum > 100:
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        remaining = total_sum - 100
        medical_staff.pop()
        medical_staff[-1] += remaining
        textiles.popleft()
    else:
        medical_staff[-1] += 10
        textiles.popleft()

if not textiles and not medical_staff:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")
if created_items:
    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for item, count in sorted_items:
        print(f"{item} - {count}")
remaining_textiles = ", ".join(str(x) for x in textiles)
if remaining_textiles:
    print(f"Textiles left: {remaining_textiles}")
remaining_medical_staff = ", ".join(str(x) for x in reversed(medical_staff))
if remaining_medical_staff:
    print(f"Medicaments left: {remaining_medical_staff}")
