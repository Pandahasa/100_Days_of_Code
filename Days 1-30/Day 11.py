import random as rand

if input("Do you want to play a game of blackjack, type 'y' or 'n': ") == "y":
    play = True
else:
    play = False

ai_score = 0
score = 0    
money = 100

def check(total, bet):
    global score
    global ai_score
    global money
    if sum(total) == 21:
        score += 1
        print(f"Your cards: {str(total)}, final score: {sum(total)}")
        print("Blackjack!! You win!")
        money += bet*2
    elif sum(total) > 21:
        ai_score += 1
        print(f"Your cards: {str(total)}, final score: {sum(total)}")
        print("Bust. You lose")
    else:
        print(f"Your cards: {str(total)}, current score: {sum(total)}")


def hit(total):
    cards = [11, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
    addon = rand.choice(cards)
    if sum(total) + addon // 21 == 1 and addon == 11:
        addon = 1
    total.append(addon)

def stand(total , ai_total , bet):
    under_17 = True
    global score
    global ai_score
    global money
    while under_17:
        hit(ai_total)
        if sum(ai_total) >= 17:
            under_17 = False
    if sum(ai_total) == sum(total):
        print("Tie." , sum(ai_total))
        money += bet
        return
    elif sum(ai_total) < sum(total):
        score += 1
        print("You win!" , sum(ai_total))
        money += bet*2
        return
    elif sum(ai_total) > 21:
        score += 1
        print("Dealer Bust!! You win!" , sum(ai_total))
        money += bet*2
        return
    elif sum(ai_total) > sum(total):
        ai_score += 1
        print("You lose." , sum(ai_total))
        return
    

while play:
    playing = True
    total = []
    ai_total = []
    if money == 0:
        print("You are Bankrupt")
        play = False
        continue
    bet = int(input(f"How much do you want to bet, you currently have ${money} remaining." ))
    if bet > money or bet <= 0:
        print("This is an invalid amount")
        continue
    money -= bet
    hit(total)
    hit(total)
    hit(ai_total)
    print(f"Computer's first card: {ai_total[0]}")
    check(total, bet)
    if sum(total) == 21 or sum(total) > 21:
        playing = False
    while playing:
        if input("Do you want to 'stand' or 'hit'?: ") == "hit":
            hit(total)
            check(total, bet)
            if sum(total) == 21 or sum(total) > 21:
                playing = False
        else:
            stand(total , ai_total , bet)
            playing = False
    if input(f"Do you want to play again 'y' or 'n'") == 'n':
        play = False

print(f"Final score {score}:{ai_score}")
        




    