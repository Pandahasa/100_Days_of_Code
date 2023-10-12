from click import clear
import day14art as art
from game_data import data
import random as rand

playing = True
score = 0
p1 = 0
p2 = 0
ongoing = False

while playing:
    clear()
    print(art.logo)
    p1 = rand.choice(data)
    if ongoing == True:
        p1 = p2
    print(f"\nCompare A: {p1['name']}, a {p1['description']}, from {p1['country']}\n")
    p2 = rand.choice(data)
    ongoing = True
    print(art.vs)
    print(f"\nAgainst B: {p2['name']}, a {p2['description']}, from {p2['country']}\n")
    answer = input("B has Higher or Lower followers than A?\n")
    if answer == "higher":
        if p1['follower_count'] < p2['follower_count']:
            score += 1
            continue
        else:
            print("Final Score: " , score)
            playing = False
    elif answer == "lower":
        if p1['follower_count'] > p2['follower_count']:
            score += 1
            continue
        else:
            print("Final Score: " , score)
            playing = False
