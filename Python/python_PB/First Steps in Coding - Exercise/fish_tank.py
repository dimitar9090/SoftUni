length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
volume = length * width * height
volume_in_liters = volume / 1000
used_space = percentage / 100
liters_needed = volume_in_liters * (1 - used_space)
print(liters_needed)