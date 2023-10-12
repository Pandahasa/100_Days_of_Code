import csv
import os
import re
import sys
import pandas

a = os.path.join(sys.path[0], 'p.csv')
data = pandas.read_csv(a)


#TODO 1. Create a dictionary in this format:1
{"A": "Alfa", "B": "Bravo"}

nato = {row.letter:row.code for (index , row) in data.iterrows()}
# for (letter , word) in data.iterrows():
#     nato[word.letter].append(word.code)

print(nato)

def phonetic():
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    useri = input("what word: ").upper()
    try:
        output = [nato[i] for i in useri]
    except KeyError:
        print("Sorry, letters only please")
        phonetic()
    else:
        print(output)

    
    
phonetic()