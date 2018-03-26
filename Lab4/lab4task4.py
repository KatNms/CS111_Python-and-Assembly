#
# name: Katrina Nemes
# email: knemes@bu.edu
#
#
# Lab 4, Task 4 -  Writing functions that use lists-of-lists
#
#

def longest_word(wordlist):
    """ returns the longest word from the wordlist passed in as 
        a parameter
    """
    pairs = [[len(w), w] for w in wordlist]
    bestpair = max(pairs)
    return bestpair[1]

def square(value):
    """provided function that takes integer value and returns the square"""
    
    sq = value**2
    return sq

def process_squares(values, choice):
    """ takes two inputs: a list of integers values and a single integer choice. It should use the list-of-lists technique and
    the square helper function to return one of two possible results
    """
    
    
