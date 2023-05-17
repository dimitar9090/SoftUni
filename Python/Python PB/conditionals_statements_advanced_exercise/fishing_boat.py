budget = int(input())
season = input()
number_of_fishermen = int(input())
price_for_ship = 0
if season == 'Spring':
    price_for_ship = 3000
elif season == 'Summer' or season == 'Autumn':
    price_for_ship = 4200
elif season == 'Winter':
    price_for_ship = 2600
if number_of_fishermen <= 6:
    price_for_ship *= 0.90
elif number_of_fishermen <= 11:
    price_for_ship *= 0.85
elif number_of_fishermen >= 12:
    price_for_ship *= 0.75
if number_of_fishermen % 2 == 0 and season != 'Autumn':
    price_for_ship *= 0.95
difference = abs(price_for_ship - budget)
if price_for_ship <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
