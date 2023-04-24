year_tax = int(input())
snicker_price = year_tax - (year_tax * 0.40)
outfit_price = snicker_price - (snicker_price * 0.20)
ball_price = outfit_price / 4
accessories_price = ball_price / 5
all_price_for_equipment = year_tax + snicker_price + outfit_price + ball_price + accessories_price
print(all_price_for_equipment)
