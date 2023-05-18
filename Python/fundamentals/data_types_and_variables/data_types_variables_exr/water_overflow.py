number_of_follows = int(input())
capacity_of_the_tank = 255
tank_fill = 0
for current_follows in range(number_of_follows):
    follow = int(input())
    if capacity_of_the_tank - follow < 0:
        print("Insufficient capacity!")
        continue
    capacity_of_the_tank -= follow
    tank_fill += follow
print(tank_fill)