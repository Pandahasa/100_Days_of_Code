print("Welcome to Treasure Island. Your mission is to find the Treasure.")
status = ("alive")

while status != "dead":
    decision = input("Left or right ").lower()
    if decision == "right":
        print("Game Over!")
        status = "dead"
    else:
        decision = input("Swim or wait ").lower()
        if decision == "swim":
            print("Game Over!")
            status = "dead"
        else:
            decision == input("Which Door? Red or Blue or Yellow? ").lower()
            if decision == "red":
                print("Game Over!")
                status = "dead"
            elif decision =="blue":
                print("Game Over!")
                status = "dead"
            else:
                print("You Win!")
                status = "dead"

    
