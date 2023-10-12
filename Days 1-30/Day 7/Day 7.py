import os
import random as rand
from hangman_art import stages, logo
from hangman_words import word_list

word = rand.choice(word_list)
game_status = True
lives = 6
print(logo)
display = []
for x in range(len(word)):
    display += ("_")

while game_status:
    letter = input("What is your guess: ")
    os.system('clear')
    for x in range(len(word)):
        if letter in word[x]:
            display[x] = letter
            print(letter)
        else:
            print(display[x])
    if letter not in word:
        print("Unfortunately" , letter , "was not in the word, so you lose a life")
        lives -= 1
        print("You have" , lives , "left")
        if lives == 0:
            game_status = False
            print("You lose :( the word was" , word)
    else:
        print("Nice" , letter , "was in the word")
        if "_" not in display:
            game_status = False
            print("You win!!! The word was" , word)

    print(stages[lives])

    
    

    