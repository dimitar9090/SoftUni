register = {}
while True:
    current_command = input()
    if current_command == "end":
        break
    course_name, student_name = current_command.split(" : ")
    if course_name not in register.keys():
        register[course_name] = [ ]
    register[course_name].append(student_name)
for course_name, student_name in register.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")


