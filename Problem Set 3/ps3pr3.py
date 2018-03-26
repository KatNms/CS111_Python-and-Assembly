#
# name: Katrina Nemes
# email: knemes@bu.edu
#
#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.


def rot(c, n):
    """ Rotates a single character, c, forward by n spots
    c: char value
    n: integer value

    returns character value
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        if ( (ord(c) + n) > ord('z')):
            new_char = chr( (ord(c) + n) - 26)
            return new_char
        else:
            new_char = chr( ord(c) + n)
            return new_char
        
    if 'A' <= c <= 'Z':
        if (ord(c) + n) > ord('Z'):
            new_char = chr( (ord(c) + n) - 26)
            return new_char
        else:
            new_char = chr( ord(c) + n)
            return new_char
                           
    else:
        return c
        

### Put your code for the encipher function below. ###
def encipher(s,n):
    """Takes input s, string value, and n, a non-negative integer between 0 and 25
    and returns a new string in which letters in s are rotated by n characters forward
    in the alphabet
    """
    

    if len(s) == 0:
        return ''
    else:
        new_string = rot(s[0],n)
        return new_string + encipher(s[1:],n)

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####

def score_help(s):
    """ helps find probablity of which phrase is most enlish
    input s is string value
    returns integer value
    """

    if s == '':
        return 0
    else:
        rest = score_help(s[1:])
        return letter_prob(s[0]) + rest

def decipher(s):
    """ Takes enciphered input, s, and returns the original/most plausible English string.
    input s: string value
    returns string value
    """

    list = [ encipher(s, n) for n in range(26) ]
    print('list of enciphers: ', list)
    score_list = [ [ score_help(x), x] for x in list]
    print('scored list: ', score_list)
    best_score = max(score_list)
    return best_score[1]
    

    
