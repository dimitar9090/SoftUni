actor_name = input()
academy_point = float(input())
number_of_jury = int(input())
total_points = academy_point
for current_grade in range(number_of_jury):
    current_name = input()
    current_point = float(input())
    final_point = len(current_name) * current_point / 2
    total_points += final_point
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = 1250.5 - total_points
    print(f' Sorry, {actor_name} you need {difference:.1f} more!')