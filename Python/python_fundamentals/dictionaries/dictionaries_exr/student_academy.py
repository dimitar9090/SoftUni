class_room = {}
number_of_students = int(input())
while number_of_students != 0:
    name_of_student = input()
    grade_of_student = float(input())
    number_of_students -= 1
    if name_of_student not in class_room:
        class_room[name_of_student] = []
    class_room[name_of_student].append(grade_of_student)
for name, grade in class_room.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

