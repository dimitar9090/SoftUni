from math import pi
figure = input()
if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    result = side2 * side1
elif figure == "circle":
    diameter = float(input())
    result = (diameter **2) * pi
elif figure == "triangle":
    side = float(input())
    height = float(input())
    result = (side * height) / 2
print(f"{result:.3f}")
