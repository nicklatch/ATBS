# Coin Flip Streaks

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    coinFlip = []
    streak = 0
#Code that creates a list of 100 'heads' or tails.
    for i in range(100):
        coinFlip.append(random.randint(0,1))
    # Code that creates a list if there is a streak of 6 heads or 'tails' values.
    for i in range(len(coinFlip)):
        if i == 0:
            pass
        elif coinFlip[i] == coinFlip[i-1]:
            streak += 1
        if streak == 6:
            numberOfStreaks += 1
print("Chance of streak: %s%%"  % (numberOfStreaks / (100 * 10000)))


