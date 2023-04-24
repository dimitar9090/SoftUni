#	Пилешко меню –  10.35 лв.
#	Меню с риба – 12.40 лв.
#	Вегетарианско меню  – 8.15 лв.
number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())
price_chicken = number_chicken_menu * 10.35
price_fish = number_fish_menu * 12.40
price_vegan = number_vegan_menu * 8.15
all_price_of_menu = price_vegan + price_fish + price_chicken
desert_price = all_price_of_menu * 0.20
delivery_price = 2.50
all_price_of_order = all_price_of_menu + desert_price + delivery_price
print(all_price_of_order)