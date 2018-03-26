#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 4
# Problem 2: Using your conversion functions
#

from ps4pr1 import *

def mul_bin(b1,b2):
    """
    Takes inputs b1 and b2 as strings that represent binary numbers.
    Multiplies the two inputs and returns the result in string form that
    represents a binary number
    """

    n1 = bin_to_dec(b1)    
    n2 = bin_to_dec(b2)

    b = dec_to_bin(n1*n2)

    return b

def add_bytes(b1,b2):
    """
    Takes inputs b1 and b2 as strings that represent bytes. Computes the sum
    of two bytes and returns the sum in the form of a string
    """

    n1 = bin_to_dec(b1)    
    n2 = bin_to_dec(b2)

    b = dec_to_bin(n1 + n2)

    if len(b) > 8:
        return b[-8:]
    elif len(b) < 8:
        differnce = 8 - len(b)
        return '0'*differnce + b
    else:
        return b
            
