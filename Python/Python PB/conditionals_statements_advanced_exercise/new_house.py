type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_of_flower == 'Roses':
    price = 5
    if number_of_flowers > 80:
        price *= 0.90
elif type_of_flower == 'Dahlias':
    price = 3.80
    if number_of_flowers > 90:
        price *= 0.85
elif type_of_flower == 'Tulips':
    price = 2.80
    if number_of_flowers > 80:
        price *= 0.85
elif type_of_flower == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        price *= 1.15
elif type_of_flower == 'Gladiolus':
    price = 2.5
    if number_of_flowers < 80:
        price *= 1.20
final_price = price * number_of_flowers
difference = abs(final_price - budget)
if budget >= final_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")