deposit_sum = float(input())
time_deposit = int(input())
year_payback_percent= float(input())
year_payback = deposit_sum * (year_payback_percent/100)
payback_per_month = year_payback/12
total_sum = deposit_sum + time_deposit * payback_per_month
print(total_sum)