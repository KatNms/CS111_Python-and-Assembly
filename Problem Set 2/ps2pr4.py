#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 2
# Problem 4: Fun with recursion, part I
#
# partner: Jenna Zhu
# partner's email: jennazhu@bu.edu
#

def copy(s, n):
    """ Takes input s, string value, and n, integer value, and uses
    recursion to create and return a string in which n copies of s
    are concatenated together
    """

    if n <= 0:
        return ''
    else:
        s_copy = copy(s, n-1)
        return s + s_copy
        
def sum(values):
    """ takes input values, list value of integers, and uses recursion to
    compute and return the sum of all integers in the list
    """

    if len(values) == 1:
        return values[0]
    elif len(values) == 0:
        return 0
    else:
        rest = sum(values[1:])
        values[0] = values[0] + rest
        return values[0]


def test():
    """ test function for the function(s) above """
    
    test1 = copy('da', 2)
    print('the first test returns', test1)

    test2 = copy('Go BU!', 4)
    print('the second test returns', test2)

    test3 = copy('hello', 1)
    print('the third test returns', test3)

    test4 = sum([1, 2, 3, 4, 5])
    print('the fourth test returns', test4)

    test5 = sum([])
    print('the fifth test returns', test5)




    
    
