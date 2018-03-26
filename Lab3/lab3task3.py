#
# Name: Katrina Nemes
#
# lab3task3.py
#

def min_val(values):
    """ Takes non-empty list of values and uses recursion to find
    and return the smallest value in the list

    paramters: values is a list
    """

    if len(values) == 1:    #if length of values is 1
        return values[0]
    else:
        rest = min_val(values[1:])  #recursively call min_val
        if values[0] < rest:        #compare values[0] to rest to see which is smaller
            return values[0]
        else:
            return rest


def test():
    """ test function for min_val() """
    test1 = min_val(['b', 'a', 'c'])
    print('test call 1 returns', test1)

    test2 = min_val([4, 10, 7, 15])
    print('test2 call 2 returns', test2)

    test3 = min_val([20, 6, 5, 10])
    print('test3 call 3 returns', test3)

    test4 = min_val([10])
    print('test4 call 4 returns', test4)
    


