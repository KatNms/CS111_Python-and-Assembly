def mysum(x, y):
    """ takes two numbers and returns their sum """
    total = x + y
    return total

#question 3: syntax error occurs
#question 5: mysum(44, 67) prints 111
#            print(mysum(10, 7)) prints 17 followed by None

def sum_double(x, y):
    """ accepts two integers and returns sum unless two values are the same, then it doubles their sum. """
    if x != y:
        return x + y
    else:
        sum = 2* (x + y)
        return sum

def test():
    """ function for testing """
    test1 = sum_double(1, 2)
    print('first test returns', test1)

    # Add more tests below

    test2 = sum_double(3, 2)
    print('second test returns', test2)

    test3 = sum_double(2, 2)
    print('third test returns', test3)

    test4 = sum_double(-2, -2)
    print('fourth test returns', test4)
        



