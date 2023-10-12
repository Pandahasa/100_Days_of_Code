print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
split = float(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = (total_bill + (tip_percentage*0.01*total_bill))
each = tip/split

print("Each person should pay:" , round(each, 2))