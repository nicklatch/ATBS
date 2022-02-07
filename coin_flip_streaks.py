# Coin Flip Streaks

import random
experimentNumber = 0
numberOfStreaks = 0
for experimentNumber in range(10000):
    coin = "h" * 50 + "t" * 50
    flip_list = random.sample(coin, 100)
    if flip_list[experimentNumber:experimentNumber + 5] == ["h", "h", "h", "h", "h", "h", ] or ["t", "t", "t", "t", "t", "t"]:
        numberOfStreaks += 1
        continue

# code that checks if there is a streak of 6 heads or 6 tails in a row.

print("Chance of streaks: %s%%" % (numberOfStreaks / 100))
