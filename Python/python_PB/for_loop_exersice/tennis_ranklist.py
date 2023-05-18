import math
number_of_tournament_played = int(input())
starting_points = int(input())
final_points = starting_points
winner_times = 0
for tournaments in range(1, number_of_tournament_played +1):
    stage_of_tournament = input()
    if stage_of_tournament == 'W':
        final_points += 2000
        winner_times += 1
    elif stage_of_tournament == 'F':
        final_points += 1200
    elif stage_of_tournament == 'SF':
        final_points += 720
average_points_for_tournament = (final_points - starting_points) / number_of_tournament_played
percentage_winner_time = (winner_times / number_of_tournament_played) * 100
print(f'Final points: {final_points}')
print(f'Average points: {math.floor(average_points_for_tournament)}')
print(f'{percentage_winner_time:.2f}%')