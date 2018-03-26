#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 4
# Problem 3: Recursive operations on binary numbers
#
#

def bitwise_and(b1,b2):
    """
    Takes inputs b1 and b2 (both string values) and uses recursion to compute bitwise AND
    of the two numbers and returns the result in the form of a string
    """

    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return '0' * len(b2)
    elif b2 == '':
        return '0' * len(b1)
    else:
        if len(b1) == len(b2):
            AndOp = str(int(b1[-1]) * int(b2[-1]))
            return bitwise_and(b1[:-1],b2[:-1]) + AndOp
        elif len(b1) > len(b2):
            difference = len(b1) - len(b2)
            b2 = '0' * difference + b2
            AndOp = str(int(b1[-1]) * int(b2[-1]))
            return bitwise_and(b1[:-1],b2[:-1]) + AndOp
        elif len(b2) > len(b1):
            difference = len(b2) - len(b1)
            b1 = '0' * difference + b1
            AndOp = str(int(b1[-1]) * int(b2[-1]))
            return bitwise_and(b1[:-1],b2[:-1]) + AndOp


def add_bitwise(b1,b2):
    """
    Takes inputs b1 and b2 (both string values) and uses recursion to perform bitwise addition and returns
    the result in string form.
    """

    carry = 0
    
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        sum_rest = add_bitwise(b1[:-1],b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return sum_rest + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return sum_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1':
            return sum_rest + '1'
        elif b1[-1] == '1' and b2[-1] == '1':
            return add_bitwise(sum_rest, '1') + '0'

                
                    
            



            
        
