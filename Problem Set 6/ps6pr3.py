# Katrina Nemes
# Problem Set 6 Problem 3: processing sequences with loops
#
# partner: Jenna Zhu
# partner's email: jennazhu@bu.edu

def double(s):
    ''' takes an arbitrary string s as input, and then uses a loop to construct and return
        the string formed by doubling each character in the string
    '''
    result = ''
    
    for c in s:
        result += (c*2)

    return result

def weave(s1,s2):
    """
    Takes two string inputs and uses a loop to construct and return a new string that weaves
    the characters in s1 and s2
    """

    result = ''
    len_shorter = min(len(s1), len(s2))

    
    for i in range(len_shorter):
        result += s1[i] + s2[i]

    if len(s1) > len(s2):
        result += s1[len_shorter:]
    elif len(s1) < len(s2):
        result += s2[len_shorter:]

    return result

def square_evens(values):
    ''' takes a list of integers called values, and then modifies the list so that all of its
        even elements are replaced by their squares, but all f its odd elements are left unchanged
    '''
    for n in range(len(values)):
        if values[n] % 2 == 0:
            values[n] = (values[n]**2)
        n += 1


def index(elem, seq):
    """
    Inputs elem and seq. Seq is either list or string. If seq is a string then elem is a single character string.
    If seq is a list then elem can be any value. Function uses a loop to find and return the index of the first
    occurence of elem in seq. Return -1 if elem is not in seq
    """

    for i in range(len(seq)):
        if seq[i] == elem:
            return i

    return -1

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('tests for double():')
    print('double(''hello''): ', double('hello'))
    print('double(''python''): ', double('python'))
    print(double('python'))
    print('double('' ''):', double(''))

    print('\n')

    print('tests for weave(s1,s2):')
    test1 = weave('aaaaaa', 'bbbbbb')
    print('aaaaaa weaved with bbbbbb:', test1)
    test2 = weave('aaaaaa', 'bb')
    print('aaaaaa weaved with bb:',test2)
    test3 = weave('aaaa', '')
    print('aaaa weaved with '' :', test3)

    print('\n')

    print('tests for square_evens(values)')    
    vals1 = [1, 2, 3, 4, 5, 6]
    print('vals1 is:', vals1)
    square_evens(vals1)
    print('square_evens(vals1) is:', vals1)
    vals2 = [7, 3, 10, 8]
    print('vals2 is:', vals2)
    square_evens(vals2)
    print('square_evens(vals2) is:', vals2)

    print('\n')

    print('tests for index(elem,seq)')
    test4 = index(5, [4, 10, 8, 5, 3, 5])
    print('elem 5 is found at index:', test4)
    test5 = index('hi', ['well', 'hi', 'there'])
    print('elem ''hi'' is found at index:', test5)
    test6 = index(8, [4, 10, 5, 3])
    print('elem 8 is not in seq. Return', test6)



    
    
