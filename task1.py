#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"
a = int(input("what number"))
if a < 100 :
    print ("number less than 100")
if a > 100 :
    print("number more than 100")
if a == 100 :
    print ("number is 100")
