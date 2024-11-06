# Marit Mallberg
# UWYO COSC 1010
# 11/5/2024
# Lab 07
# Lab Section: 10
# Sources, people worked with, help given to:Paige Elmstrand, Serena Skaff, lab tas. 
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def numberswitch(string):
    """switch a number into it's integer of float value"""
    isneg = False
    if string[0] == "-":
        isneg = True
        string = string.replace("-","")
    if "." in string:
        nums=string.split(".")
        if len(nums)==2 and nums[0].isdigit() and nums[1].isdigit:
            if isneg:
                return -1*float(string)
            else:
                return float(string)
    elif string.isdigit():
        if isneg:
            return -1*int(string)
        else:
            return int(string)
    else:
        return False
        
    

my_number = "-170"
my_float = "3.33"
error_check = "cat"

print(numberswitch(my_number))
print(numberswitch(my_float))
print(numberswitch(error_check))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,l,u):
    """gives all func values in range a to b"""
    valuelist=[]
    for numb in range(l,(u+1)):
        value = m*numb + b
        valuelist.append(value)
    print(valuelist)


while True:
    inputs=input("give me a slope, y-intercept, and an upper and lower bound. enter 'exit' to exit")
    if inputs.lower() == "exit":
        break
    inputs=inputs.replace(" ","")
    numlist = inputs.split(",")
    len_check=True
    if len(numlist) != 4:
        len_check=False
    diglist=[]
    for num in numlist:
        num=numberswitch(num)
        diglist.append(num)
    upperfloatcheck = True
    if type(diglist[2]) == float:
        upperfloatcheck = False
    lowerfloatcheck= True
    if type(diglist[3]) == float:
        lowerfloatcheck = False
    boundcheck = True

    if diglist[2]<diglist[3]:
        boundcheck = False
    slope_intercept(diglist[0],diglist[1],diglist[2],diglist[3])

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqrt(n):
    """the sqrt function"""
    if n<0:
        return None
    return n**(1/2)

def quadformula(a,b,c):
    """ solves the quadratic formula for x-intercepts"""
    answers = []
    bsqed= b**2
    fourac=4*a*c
    twoa = 2*a

    insidesqrt = bsqed-fourac
    
    if insidesqrt < 0:
        print("complex roots, no clear answer.")
        return

    root = sqrt(insidesqrt)
    xplus=(-b+root)/twoa
    answers.append(xplus)
    xminus = (-b-root)/twoa
    answers.append(xminus)
    print(answers)

while True:
    equation = input("give me the a, b, and c of a quadratic equation, type 'exit' to exit")
    if equation.lower() == "exit":
        break
    equation = equation.replace(" ", "")
    equlist = equation.split(",")
    numlist = []
    for equ in equlist:
        equ = numberswitch(equ)
        numlist.append(equ)
    quadformula(numlist[0],numlist[1],numlist[2])







