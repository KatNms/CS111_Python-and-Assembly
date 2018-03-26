def print_forward(s):
    """ Takes input string s and uses recursion to print the string character
    by character

    paramter: s is a string value
    """
    if s == '':     #base case, nothing is left in the string
        print()

    else:
        print(s[0])
        rest = print_forward(s[1:])

def print_backward(s):
    """ Takes input string s and uses recursion to print the string s character by character
    in the reverse order

    paramter: s is a string value
    """
    if s == '':     #base case, nothing is left in the string
        print()

    else:
       print(s[-1])
       rest = print_backward(s[:-1])

#test cases for print_forward(s)
print('three test cases for print_forward(s) function')
print()

print_forward('computer')
print_forward('science')
print_forward('bedtime')

print('three test cases for print_backward(s) function')
print()

print_backward('computer')
print_backward('science')
print_backward('bedtime')
        
    
