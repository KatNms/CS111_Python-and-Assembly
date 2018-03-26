#
# name: Katrina Nemes
# email: knemes@bu.edu
#
#
# Lab 4, Task 2 - debugging a recursive function
#
#

def count(val, values):
    """ returns the number of times that val is found in the list values
        parameters:
            val -- an arbitrary value
            values -- a list of 0 or more arbitrary values
    """
    if len(values) == 0:            # change base case because it is redundant. 
        return 0                    # if you've tested all values in list then return 0
    else:
        count_in_rest = count(val, values[1:])  # change so that it increments one value to the right each time
        if values[0] == val:
            return count_in_rest + 1            # add to count_in_rest if you've found a match
        else:
            return count_in_rest                # else return count_in_rest and evaluate next recursion
