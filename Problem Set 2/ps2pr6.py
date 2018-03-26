#
# name: Katrina Nemes
# email: knemes@bu.edu
#
# ps2pr6.py - Problem Set 2, Problem 6
#
# list comprehensions
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [  x * 2      for x in range(5)]
print(lc1)


# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [  w[1]     for w in words]
print(lc2)

# part c
lc3 = [ word[::-1]*2        for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [   x**2       for x in range(1, 10) if       x%2 == 0      ]
print(lc4)

# part e
lc5 = [ (c == 'b' or c == 'u')    for c in 'bu be you']
print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.
def powers_of(base, count):
    """Takes input base and positive integer count, both integer values
    and uses list comprehension to construct and return a list containing
    the first count powers of base, beginning the 0th power
    """
    
    
    powers_list = [ base ** count for count in range(0, count)]
    return powers_list


# Problem 5-3: Put your definition of the shorter_than() function below.
def shorter_than(n, wordlist):
    """ Takes inputs as integer n and list of strings wordlist. Uses list comprehension
    to construct and return a list consisiting of all words from wordlist that are shorter than n
    """

    shorter_list = [word for word in wordlist if (len(word) < n)]
    return shorter_list


