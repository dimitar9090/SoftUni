number_of_iterations = int(input())
left_sum = 0


for i in range( number_of_iterations):
    left_sum += int(input())
right_sum = 0
for i in range(number_of_iterations):
    right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')

