#
# name: Katrina Nemes
# email: knemes@bu.edu
#
#
# Lab 4, Task 3 - Designing a recursive function
#
#

def remove_spaces(s):
    """ Takes input s (string value) and uses recursion to construct and return a string
    in which all spaces have been removed
    """

    if len(s) == 0:
        return ''
    else:
        #print('s is now: ', s[0])

        if s[0] == ' ':
            return remove_spaces(s[1:])
        else:
            
            return s[0] + remove_spaces(s[1:])




