rows, columns = map(int, input().split())
playground = [input().split() for _ in range(rows)]
row, col = 0, 0
for i in range(rows):
    for j in range(columns):
        if playground[i][j] == 'B':
            row, col = i, j

number_of_opponents = 3
moves = 0
while number_of_opponents > 0:
    current_command = input()
    if current_command == "Finish":
        break

    if current_command == "up":
        if row - 1 >= 0 and playground[row-1][col] != 'O':
            row -= 1
            if playground[row][col] == 'P':
                number_of_opponents -= 1
                moves += 1
                playground[row][col] = '-'
            else:
                moves += 1

    elif current_command == "down":
        if row + 1 < rows and playground[row + 1][col] != 'O':
            row += 1
            if playground[row][col] == 'P':
                number_of_opponents -= 1
                moves += 1
                playground[row][col] = '-'
            else:
                moves += 1

    elif current_command == "left":
        if col - 1 >= 0 and playground[row][col-1] != 'O':
            col -= 1
            if playground[row][col] == 'P':
                number_of_opponents -= 1
                moves += 1
                playground[row][col] = '-'
            else:
                moves += 1

    elif current_command == "right":
        if col + 1 < columns and playground[row][col + 1] != 'O':
            col += 1
            if playground[row][col] == 'P':
                number_of_opponents -= 1
                moves += 1
                playground[row][col] = '-'
            else:
                moves += 1

print("Game over!")
print(f"Touched opponents: {3 - number_of_opponents} Moves made: {moves}")
