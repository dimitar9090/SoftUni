number_of_floors = int(input())
number_of_rooms = int(input())
room_number = 0
room_name = ''
for x in range(number_of_floors, 0, -1):
    for j in range(number_of_rooms):
        room_number = x * 10 + j
        if x == number_of_floors:
            room_name = f'L{room_number}'
        elif x % 2 != 0:
            room_name = f'A{room_number}'
        elif x % 2 == 0:
            room_name = f'O{room_number}'
        print(room_name, end=' ')
    print()
