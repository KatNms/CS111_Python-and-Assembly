#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 3
# Problem 4: More algorithm design!
#
#

def rem_last(elem, values):
    """ takes inputs elem and values and uses recursion to create and return a version of
    values in which the last occurance of elem has been removed

    elem: integer value
    values: list of values
    """

    if len(values) == 0:
        return []

    elif values[-1] == elem:
        return values[:-1]

    else:
        return rem_last(elem, values[:-1]) + [values[-1]]


def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values

    helper function for jscore(s1,s2)
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest

    
                
def jscore(s1,s2):
    """ takes s1 and s2 as inputs and returns the Jotto score of s1 compared with s2.
    s1 & s2 are both string values
    return value is an integer

    note: Jotto is the number of characters shared in both strings
    """

    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[0] in s2:
            next_char = rem_first(s1[0], s2)
            #print(next_char)
            return jscore(s1[1:], next_char) + 1
        else:
            next_char = rem_first(s1[0], s2)
            return jscore(s1[1:], next_char)
        


def lcs(s1,s2):
    """ Takes s1 and s2 and returns the longest common subsequence they share.
    s1 & s2 are string values
    return value is also a string
    """

    if len(s1) == 0 or len(s2) == 0:
        return ''
    else:
        if s1[0] == s2[0]:
            #print('s1[0] & s2[0]: ', s1[0])
            return s1[0] + lcs(s1[1:], s2[1:])
        else:
            #next_char = rem_first(s1[0], s2)
            #print('s1[0]: ', s1[0], 'and s2[0]: ', s2[0] )
            result1 = lcs(s1[1:], s2)
            result2 = lcs(s1, s2[1:])
            #print('string is either: ', result1, result2)

            best_result = max( [len(result1), result1], [len(result2), result2] )           
            return best_result[1]
        


