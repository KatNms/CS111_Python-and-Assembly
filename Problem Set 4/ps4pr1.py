#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 4
# Problem 1: From binary to decimal and back!
#
# partner's name: Jenna Zhu
# partner's emai: jennazhu@bu.edu
#

def dec_to_bin(n):
    """
    Takes non-negative integer n and uses recursion to convert it to binary.
    Returns string version of binary representation
    """

    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        if n % 2 == 0:
            return dec_to_bin(n//2) + '0'   #n is even
        else:
            return dec_to_bin(n//2) + '1'   #n is odd

        
    
def bin_to_dec(b):
    ''' takes a string b that represents a binary number
        uses recursion to convet the number from binary to decimal
        returning the resulting integer
    '''

    if len(b) == 1:
        if b == '1':
            return 1
        elif b == '0':
            return 0
    else:
        end = len(b) - 1
        if b[end] == '0':
            #even
            return (2 * bin_to_dec(b[:-1]) + 0)
        elif b[end] == '1':
            #odd
            return (2 * bin_to_dec(b[:-1]) + 1)
