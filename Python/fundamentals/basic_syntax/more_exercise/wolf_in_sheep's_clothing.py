the_animals = input().split(", ")
for index, animal in enumerate(the_animals):
    if animal == "wolf" and index == (len(the_animals) - 1):
        print("Please go away and stop eating my sheep")
    elif animal == "wolf":
        print(f"Oi! Sheep number {abs(index - 5)}! You are about to be eaten by a wolf!")

