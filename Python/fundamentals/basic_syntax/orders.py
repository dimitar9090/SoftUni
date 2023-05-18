number_of_orders = int(input())
total_price = 0
for current_day in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    coffee_price = price_per_capsule * days * capsules_per_day
    if price_per_capsule < 0.01 or\
            price_per_capsule > 100.00 or\
            days < 1 or days > 31 or\
            capsules_per_day < 1 or\
            capsules_per_day > 2000:
        continue
    total_price += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total_price:.2f}")


