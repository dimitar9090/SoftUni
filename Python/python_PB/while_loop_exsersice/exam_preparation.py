number_failed_grades = int(input())
failed_times = 0
current_problem = input()
solved_problems_counter = 0
average_grade = 0
last_problem = ' '
has_failed = False
while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        failed_times += 1
        if failed_times == number_failed_grades:
            has_failed = True
            break
    average_grade += current_grade
    solved_problems_counter += 1
    last_problem = current_problem
    current_problem = input()
if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f'Average score: {(average_grade / solved_problems_counter):.2f}')
    print(f'Number of problems: {solved_problems_counter}')
    print(f'Last problem: {last_problem}')
