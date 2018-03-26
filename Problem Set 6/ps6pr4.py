#
# Katrina Nemes
# knemes@bu.edu
#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# Estimating the value of pi
#
# Computer Science 111    
#

import random  
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###

### IMPORTANT NOTES:
###  - One of your functions must use a for loop, and the other function 
###    must use a while loop. You should decide which type of loop is 
###    more appropriate for each function.
###
###  - Each function must call throw_dart() from inside its loop. 
###    For full credit, each function must have *EXACTLY ONE* line of
###    code that calls throw_dart(). If a given function has fewer 
###    or more than one line of code that calls throw_dart(), you 
###    will lose points. 
###
###    In addition, your functions must *NOT* make their own calls 
###    to random.uniform(), and you will lose points if they do so.

def est_pi1(n):
    """
    Input n is a positive integer and returns an estimate of pi that is based on
    n randomly thrown darts. The return value is an int. Uses a for loop.

    Prints the following:
    - number of darts thrown so far
    - number of darts that have hit the circle
    - current estimate of pi
    """
    #area of circle = (# of darts that hit the circle * area of square) / total # of darts thrown

    hitCount = 0
    
    for i in range(n):
        if ( throw_dart() ):
            #if return value is true
            hitCount +=1
            pi = (hitCount * 4) / (i+1)
            
            print(hitCount,'hits out of', i,'throws so that pi is', pi)

        else:
            #if return value is false
            hitCount += 0
            pi = (hitCount * 4) / (i+1)

            print(hitCount,'hits out of', i,'throws so that pi is', pi)

    return pi

def est_pi2(error):
    """
    Input error is a positive floating point input and returns the number of dart throws needed to product
    an estimate of pi that is less than error away from the actual value of pi. Uses while loop.
    """
    pi = math.pi
    est = 0
    difference = pi - est
    hitCount = 0
    i = 0

    while abs(difference) > error:
        if ( throw_dart() ):
            #return value true
            i += 1
            hitCount += 1
            est = (hitCount * 4) / i
            difference = pi - est
            print(hitCount,'hits out of', i,'throws so that pi is', est)

        else:
            #return value false
            i += 1
            hitCount += 0
            est = (hitCount *4) / i
            difference = pi - est
            print(hitCount,'hits out of', i,'throws so that pi is', est)
            

    return i
            

        



















    

        
