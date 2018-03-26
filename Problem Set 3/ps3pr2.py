#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# Problem Set 3
# Problem 2: Algorithm design
#
# partner's name: Jenna Zhu
# partner's email: jennazhu@bu.edu
#

def abs_list_lc(values):
    """ Takes input values, list of integers, and uses list comprehension, in
    addition to the built in abs function to create and return
    a list containing the absolute value of the numbers in values
    """

    lc = [ abs(x) for x in values]
    return lc

def abs_list_rec(values):
    """ Takes input values, list of integers, and uses recursion to create and return
    a list containing the absolute values of the numbers in values
    """

    if len(values) == 0:
        return []
    else:
        rest = abs_list_rec(values[1:])
        return [abs(values[0])] + rest

def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_vowels(words):
    """ Takes input words, list of strings, and returns the string in the list with the
    most vowels

    uses list comprehension
    """

    lc = [ [num_vowels(x), x] for x in words ]
    most_v = max(lc)
    return most_v[1]

def num_multiples(m, values):
    """ Takes input m, integer, and values, list of integers, and returns the number of
    integers in values that are multiples of m

    uses recursion
    """


    if len(values) == 0:
        return 0
    else:
        rest = num_multiples(m, values[1:])
        if values[0] % m == 0:
            return rest + 1
        else:
            return rest

def message(name, age):
    """ takes input name, string value, and age, integer, and returns a string that is a
    personalized message based on the values of the two parameters
    """

    if age < 1:
        message = name + ' very funny!'
    elif age in range(1,10):
        message = name + ' you should no be using a computer!'
    elif age in range(10,14):
        message = name + ' welcome to the dweeb years!'
    elif age in range(15, 18):
        message = name + ' get ready for the college essays!'
    elif age in range(18, 21):
        difference = 21 - age
        if difference == 1:
            message = name + ' you have to wait ' + str(difference) + ' more year to be legal!'
        else:
            message = name + ' you have to wait ' + str(difference) + ' more years to be legal!'
    elif age == 21:
        message = name + ' congrats! But be smart!'
    elif age in range(22,30):
        message = name + ' downhill from here!'
    else:
        message = name + ' stinks for you!'
        
    return message








    
    

    
    
