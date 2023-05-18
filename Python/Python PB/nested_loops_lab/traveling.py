destination = input()
while destination != 'End':
    minimum_budget = float(input())
    sum_counter = 0
    while sum_counter < minimum_budget:
        money = float(input())
        sum_counter += money
        if sum_counter >= minimum_budget:
            print(f'Going to {destination}!')
    destination = input()
