import csv
import os
import re
import sys
a = os.path.join(sys.path[0], '2018.csv')

import pandas

data = pandas.read_csv(a)


grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "Fur_Color": ["grey" , "red" , "black"] ,
    "Count": [grey_squirrel_count , red_squirrel_count , black_squirrel_count]
}

df = pandas.DataFrame(squirrel_count)

df.to_csv("balls")
