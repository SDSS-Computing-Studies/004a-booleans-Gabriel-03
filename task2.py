#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
a = int(input("what number"))
if a < 0 :
    print ("negative")
if a > 0 :
    print("positive")
if a == 0 :
    print ("zero")
