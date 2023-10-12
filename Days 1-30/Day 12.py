import random as rand

number = (rand.randint(1,100))

print("Guess the number from 1-100")
guess = int(input("\nGuess here "))
tries = 1

while guess != number:
    tries += 1
    if guess > number:
        print("\nToo bad, try again, the number is less than your guess", )
        guess = int(input("\nGuess here "))
    elif guess < number:
        print("\nToo bad, try again, the number is greater than your guess", )
        guess = int(input("\nGuess here "))

if guess == number:
        print("\nYou did it, the number was" , number, ", it took you" , tries , "tries")