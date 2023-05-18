exam_hours = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
time_of_exam = exam_hours * 60 + exam_minutes
time_of_arrive = arrive_hour * 60 + arrive_minutes
if time_of_arrive > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arrive <= time_of_exam:
    print('On time')
elif time_of_exam - 30 > time_of_arrive:
    print('Early')
diff = abs(time_of_exam - time_of_arrive)
hour = diff // 60
minutes = diff % 60
if time_of_exam - 60 < time_of_arrive < time_of_exam :
    print(f"{minutes} minutes before the start")
elif time_of_exam - 60 >= time_of_arrive:
    print(f"{hour}:{minutes:02d} hours before the start")
elif time_of_exam + 60 > time_of_arrive > time_of_exam:
    print(f"{minutes} minutes after the start")
elif time_of_exam + 60 <= time_of_arrive:
    print(f"{hour}:{minutes:02d} hours after the start")