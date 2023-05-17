days = int(input())
room = input()
rating = input()
nights = days - 1
price = 0

if room == 'room for one person':
    price = 18
elif room == 'apartment':
    price = 25
    if nights < 10:
        price *= 0.70
    elif 10 <= nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.50
elif room == 'president apartment':
    price = 35
    if nights < 10:
       price *= 0.90
    elif 10 <= nights <= 15:
        price *= 0.75
    elif nights > 15:
        price *= 0.80
if rating == 'positive':
    price *= 1.25
elif rating == 'negative':
    price *= 0.90
final_price = nights * price
print(f"{final_price:.2f}")
