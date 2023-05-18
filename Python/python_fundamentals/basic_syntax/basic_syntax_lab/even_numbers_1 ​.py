n = int(input())
for n in range(n):
    n = int(input())
    if n % 2 != 0:
        print(f"{n} is odd!" )
        break
else:
    print("All numbers are even.")