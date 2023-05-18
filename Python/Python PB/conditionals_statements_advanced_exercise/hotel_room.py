month = input()
number_of_nights = int(input())
studio_price = 0
apartment_price = 0
if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 14 >= number_of_nights > 7:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
if number_of_nights > 14:
    apartment_price *= 0.90
final_price_apartment = number_of_nights * apartment_price
final_price_studio = number_of_nights * studio_price
print(f"Apartment: {final_price_apartment:.2f} lv.")
print(f"Studio: {final_price_studio:.2f} lv.")