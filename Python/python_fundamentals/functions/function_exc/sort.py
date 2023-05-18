def sorting(current_number):
    return list(sorted(map(int, current_number)))


numbers = input().split(" ")
print(sorting(numbers))