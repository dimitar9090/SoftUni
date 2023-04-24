trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
tracks = int(input())
all_puzzles = puzzles * 2.60
all_dolls = dolls * 3
all_teddy_bears = teddy_bears * 4.10
all_minions = minions * 8.20
all_tracks = tracks * 2
total_price = all_tracks + all_puzzles + all_minions + all_dolls + all_teddy_bears
total_count = puzzles + dolls + teddy_bears + minions + tracks
if total_count >= 50:
    total_price = total_price * 0.75
toys_price = total_price * 0.90
diff = abs(toys_price - trip_price)
if trip_price <= total_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")