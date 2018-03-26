#
# Name: Katrina Nemes
#
# lab3task2.py
#

def num_consonants(s):
    """ returns the number of consonants in s
        parameter: s is a string of lower-case letters
    """
    print('num_consonants has been called')
    
    if s == '':     #'' is empty string
        print('the string is empty')
        return 0
    else:
        num_in_rest = num_consonants(s[1:])
        if s[0] not in 'aeiou':
            print(s[0],' is not a vowel')
            return 1 + num_in_rest      #increment if not a vowel
        else:
            print(s[0], ' is a vowel')
            return 0 + num_in_rest      #add 0 if vowel

#test if it works
print('hello has', num_consonants('hello'), 'consonants')
print('computer has',num_consonants('computer'), 'consonants')
