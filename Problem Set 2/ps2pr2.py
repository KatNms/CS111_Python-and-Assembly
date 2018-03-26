#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 2
# Problem 2: More practice with writing functions
#

def mirror(s):
    """ Takes input s, string value, and returns a mirrored version of s
    that is twice the length of the original string
    """

    mirrored_string = s + s[::-1]

    return mirrored_string

def is_mirror(s):
    """ takes input s, string value, and returns True if s is a mirrored
    string and False if otherwise
    """

    if len(s) % 2 == 0:
        length_s = len(s) // 2
        
        if s[:length_s] == s[len(s)-1:length_s-1:-1]:
            #compares first half of s to unmirrored other half of s
            return True
        else:
            return False
        
    else:
        return False

def test():
    """ tests the above functions """

    test1 = mirror('bacon')
    print('the first test returns', test1)

    print()
    
    test2 = is_mirror('baconnocab')
    print('the second test returns', test2)


    test3 = is_mirror('XYZZYY')
    print('the third test returns', test3)


