#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/sidpa/OneDrive/Documents/Virtual Studio Code/100 Days of Code/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        name = name.strip()
        with open("C:/Users/sidpa/OneDrive/Documents/Virtual Studio Code/100 Days of Code/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
            letter = file.read()
            path = "C:/Users/sidpa/OneDrive/Documents/Virtual Studio Code/100 Days of Code/Day 24/Mail Merge Project Start/Input/Output/" + "Letter for " + name + ".txt"
            with open(path) as file:
                letter = letter.replace("[name]" , name)
                file.write(letter)
