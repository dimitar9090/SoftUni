numbers_of_people = int(input())
capacity = int(input())
number_courses = numbers_of_people // capacity
if numbers_of_people % capacity != 0:
    number_courses += 1
print(number_courses)
