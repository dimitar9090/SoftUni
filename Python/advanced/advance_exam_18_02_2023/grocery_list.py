def shop_from_grocery_list(budget, grocery_list_of_products, *products):
    total_price = 0
    bought_items = []
    
    for product in products:
        type_product, price = product
        if type_product in bought_items:
            continue
        if type_product not in grocery_list_of_products:
            continue
        if price > budget - total_price:
            break

        bought_items.append(type_product)
        total_price += price
    if set(grocery_list_of_products) == set(bought_items):
        money_left = budget - total_price
        return f"Shopping is successful. Remaining budget: {money_left:.2f}."
    else:
        missing_items = set(grocery_list_of_products) - set(bought_items)
        missing_items_string = ', '.join(f'{item}' for item in sorted(missing_items))
        return f"You did not buy all the products. Missing products: {missing_items_string}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))