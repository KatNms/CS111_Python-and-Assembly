# 
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# name: Katrina Nemes
# email: knemes@bu.edu
#

def replace_prefix(word, prefix):
    """ Takes a word and prefix strings and returns a string in which prefix
    replaces the characters of word up to the length of prefix
    """
    length_prefix = len(prefix)
    length_word = len(word)
    
    if length_prefix > length_word:
        return prefix

    #print(word[:length_prefix])
    word = prefix + word[length_prefix:]

    return word

def swap_halves(s):
    """ takes s and returns a string whose first half is s' second half
    and whose second half is s' first half
    """

    half_s = len(s) // 2
    
    first_half = s[0: half_s]
    new_word = s[half_s:] + first_half 

    return new_word

def statistics(list_of_int):
    """takes input of exactly 3 integers and retrns list of sum, average value,
    smallest value, largest value
    """

    if len(list_of_int) > 3:
        print('Input must be exactly 3 integers')
        return list_of_int

    my_sum = list_of_int[0] + list_of_int[1] + list_of_int[2]

    average_value = my_sum / 3


    if list_of_int[0] > list_of_int[1]:
        smallest_value = list_of_int[1]
        largest_value = list_of_int[0]

        if list_of_int[1] > list_of_int[2]:
            smallest_value = list_of_int[2]

        elif list_of_int[2] > list_of_int[0]:
            largest_value = list_of_int[2]
            
    elif list_of_int[1] > list_of_int[0]:
        smallest_value = list_of_int[0]
        largest_value = list_of_int[1]

        if list_of_int[0] > list_of_int[2]:
            smallest_value = list_of_int[2]

        elif list_of_int[2] > list_of_int[1]:
            largest_value = list_of_int[2]
    

    return [my_sum, average_value, smallest_value, largest_value]
    

    

    
