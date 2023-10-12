import random as rand

print("Lets play Rock, Paper, Scissors")

score = 0
comp_score = 0
decision = ""
while decision != "exit":
    decision = input("\nChoose either Rock, Paper, or Scissors ").lower()
    comp_decision = rand.randint(1,3)
    if comp_decision == 1:
        comp_decision = "rock"
    elif comp_decision == 2:
        comp_decision = "paper"
    else:
        comp_decision = "scissors"
    if decision == comp_decision:
        print("\nYou both selected" , decision)
        print("If you want to stop say exit")
    elif decision == "rock" and comp_decision == "paper":
        comp_score += 1
        print("\nComputer chose" , comp_decision, "so you lose this round")
        print("If you want to stop say exit")
    elif decision == "rock" and comp_decision == "scissors":
        score += 1
        print("\nComputer chose" , comp_decision, "so you win this round")
        print("If you want to stop say exit")
    elif decision == "paper" and comp_decision == "rock":
        score += 1
        print("\nComputer chose" , comp_decision, "so you win this round")
        print("If you want to stop say exit")
    elif decision == "paper" and comp_decision == "scissors":
        comp_score += 1
        print("\nComputer chose" , comp_decision, "so you lose this round")
        print("If you want to stop say exit")
    elif decision == "scissors" and comp_decision == "rock":
        comp_score += 1
        print("\nComputer chose" , comp_decision, "so you lose this round")
        print("If you want to stop say exit")
    elif decision == "scissors" and comp_decision == "paper":
        score += 1
        print("\nComputer chose" , comp_decision, "so you win this round")
        print("If you want to stop say exit")

print("\n\nThe score ended at" , score , "-" , comp_score)
if score == comp_score:
    print("You and computer tied with" , score , "points")
elif score < comp_score:
    print("Computer scored" , comp_score - score , "more points than you, so you lose")
else:
    print("You scored" , score - comp_score , "more points than the computer, so you win!")