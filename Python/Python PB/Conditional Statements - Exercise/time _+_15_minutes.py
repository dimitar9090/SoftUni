hour = int(input())
minutes = int(input())
total_minutes = hour * 60 + minutes + 15
final_hour = total_minutes // 60
final_minute = total_minutes % 60
if final_hour > 23:
    final_hour = 0
if final_minute < 10:
    print(f"{final_hour}:0{final_minute}")
else:
    print(f"{final_hour}:{final_minute}")

