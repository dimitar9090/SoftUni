n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]
primary, secondary = 0, 0
for r in range(n):
    primary += matrix[r][r]
    secondary += matrix[n - r - 1][r]
print(abs(primary - secondary))
