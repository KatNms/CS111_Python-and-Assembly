# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Jenna Zhu 
# partner's email: jennazhu@bu.edu
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
#function 1
def cube(x):
    """ takes x and returns x raised to power of 3. """
    return x**3

#function 2
def compare(num1, num2):
    """ takes num1 and num2 and returns value based on how
    the nummbers compare (i.e. 1, 0, -1)
    """
    if num1 == num2:
        return 0
    elif num1 > num2:
        return 1
    else:
        return -1

#function 3
def convert_from_inches(inches):
    """ takes nonnegative integer inches and returns list of three
    integers in which that length was broken up into yards, feet,
    and inches.
    """
    if inches < 0:
        print('Input must be nonnegative')
        return
    
    yards = 0     #1 yard = 36 inches
    feet = 0      #1 foot = 12 inches

    if inches >= 36:
        yards = inches // 36
        inches = inches - (36*yards)

        if inches >= 12:
            feet = inches // 12
            inches = inches - (12*feet)

    elif inches >= 12:
        feet = inches // 12
        inches = inches - (12*feet)

      
    return [yards, feet, inches]
        


    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    print()
    # optional but encouraged: add test calls for your functions below

    print('cube(x) retuns ', cube(2))
    print()
    
    print('compare(5,2) ', compare(5,2))
    print('compare(2,5) ', compare(2,5))
    print('compare(2,2) ',compare(2,2))
    print()
    
    print('convert_from_inches(67)', convert_from_inches(67))
    print('convert_from_inches(75)', convert_from_inches(75))
    print()
    

