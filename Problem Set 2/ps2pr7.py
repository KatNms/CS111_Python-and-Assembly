#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 2
# Problem 7: Fun with recursion, part II
#
#

def letter_score(letter):
    """ Takes a lowercase letter as input, string value, and returns the value of that
    letter as a scrabble tile. If letter is not a lowercase letter from 'a' to 'z' then
    the function returns 0.
    """

    assert(len(letter) == 1)
    

    if letter == 'a' or letter =='n' or letter =='o' or letter =='e' or letter =='r' or letter =='s' or letter =='t' or letter =='u' or letter =='i' or letter =='l':
        return 1
    
    elif letter == 'b' or letter =='c' or letter =='p' or letter =='m':
        return 3

    elif letter == 'd' or letter =='g':
        return 2

    elif letter ==  'q' or letter =='z':
        return 10

    elif letter == 'f' or letter =='h' or letter =='v' or letter =='w' or letter =='y':
        return 4

    elif letter == 'j' or letter =='x':
        return 8

    elif letter == 'k':
        return 5

    else:
        return 0

def scrabble_score(word):
    """ Takes input word, string value, which contains only lower case letters and uses recursion
    to compute and return the scrabble score of the string
    """
    value = 0

    if word == '':
        return value
    else:
        rest = scrabble_score(word[1:])
        value = letter_score(word[0])
        #print(value)
        return value + rest

def index(elem, seq):
    """ takes inputs as element elem and sequence seq and uses recursion to find and return the
    index of the first occurence of elem in seq.

    Seq is either a list or a string. if string, elmen is a single char string.
    if seq is a list, elem can be any value
    """
    value = 0
    count = 0

    if seq == [] or seq == '':
        return value
    else:
        rest = index(elem, seq[1:])
        count = count + 1
        if elem == seq[0]:
            return count

        else:
            return -1
    


def test():
    """ test function for the functions above """
    test1 = letter_score('w')
    print('the first test returns', test1)

    test2 = scrabble_score('hello')
    print('the second test returns', test2)

    test3 = index(5, [4, 10, 5, 3, 7, 5])
    print('the third test returns', test3)
    
    










