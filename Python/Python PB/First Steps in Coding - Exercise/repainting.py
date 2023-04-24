nylon = int(input())
paint = int(input())
liquid = int(input())
hours = int(input())
price_nylon = (nylon + 2) * 1.50
price_paint = (paint * 1.10) * 14.50
price_liquid = liquid * 5.00
price_bag = 0.40
price_all_supplies = price_bag + price_paint + price_nylon + price_liquid
price_master = (price_all_supplies * 0.30) * hours
final_price = price_all_supplies + price_master
print(final_price)
