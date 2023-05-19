size = int(input())
matrix = [[int(x) for x in input().split(", ")]for _ in range(size)]
primary_diagonal = [matrix[r][r]for r in range(size)]
secondary_diagonal = [matrix[size - r - 1][r] for r in range(size - 1, -1, -1)]
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")