word = input().lower()
counter = 0
beach_things = ["sand", "water", "fish", "sun"]
for w in beach_things:
    if w in word:
        w_counter = word.count(w)
        counter += w_counter
print(counter)