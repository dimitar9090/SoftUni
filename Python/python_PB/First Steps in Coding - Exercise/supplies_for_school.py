#	Брой пакети химикали - цяло число в интервала [0...100]
#	Брой пакети маркери - цяло число в интервала [0...100]
#   Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#	Процент намаление - цяло число в интервала [0...100]


pens = int(input())
markers = int(input())
liquid_for_board = int(input())
pr_discount = int(input())
#	Пакет химикали - 5.80 лв.
#	Пакет маркери - 7.20 лв.
#	Препарат - 1.20 лв (за литър)
price_pens = pens * 5.80
price_markers = markers * 7.20
price_liquid = liquid_for_board * 1.20
price_all_supplies = price_pens + price_liquid + price_markers
price_with_discount = price_all_supplies - (price_all_supplies * pr_discount/100)
print(price_with_discount)