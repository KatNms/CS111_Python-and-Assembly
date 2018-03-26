# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# name: Katrina Nemes
# email: knemes@bu.edu
#

def front3(s):
    """If the string length is less than 3, the front is whatever is there.
    Return a new string which is 3 copies of the front
    """
    if len(s) >= 3:
        return (s[:3]*3)
    else:
        return (s*3)

def shorter_len(l1, l2):
    """Takes two lists and returns the length of the shorter list """
    if len(l1) < len(l2):
        return len(l1)
    elif len(l1) > len(l2):
        return len(l2)
    else:
        return len(l1)  # if both lists have the same length

def ends_with(word, suffix):
    """ Takes two strings and returns true if word strng ends with suffix string
    and false if otherwise
    """
    length_suffix = len(suffix)
    length_word = len(word) - length_suffix
    
    if suffix in word[length_word:] :
        return True
    else:
        return False
        
