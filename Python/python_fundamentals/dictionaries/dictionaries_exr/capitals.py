countries = input().split(", ")
capitals = input().split(", ")
my_final_print = dict(zip(countries, capitals))
for country, capital in my_final_print.items():
    print(f"{country} -> {capital}")