#
# Katrina Nemes
# knemes@bu.edu
#
# ps6pr5.py
#

def fib(n):
    """
    Input n is an integer. A loop is used to determine and print the first n Fibonacci numbers
    as well as compute and return the sum of those numbers
    """

    a = 0
    b = 1
    sum = 1
    print(1)

    for i in range(1,n):
        aOld = a
        a = b
        b += aOld
        print(b)
        sum += b

    return sum

def main():
    """
    - asks user how many Fibonacci numbers to product
    - call fib function
    - print sum of numbers (fib return value)
    """

    produce = int(input('How many Fibonacci numbers would you like? '))
    
    result = fib(produce)
    print('their sum is',result)
    
    






        
