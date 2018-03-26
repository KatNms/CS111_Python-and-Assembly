# Katrina Nemes
#
# Lab 7, Task 2
#
# Computer Science 111
#

# Katrina Nemes
# knemes@bu.edu

# Lab 7 Task 1: write functions that use a loop


def find_max_goals(goals):
    """ returns the largest number of goals in the specified 
        list of goals, which we assume contains at least one integer
    """
    maxg = goals[0]

    for g in goals:
        if g > maxg:
            maxg = g

    return maxg

def find_num_wins(bruins,opponents):
    """ Takes two lists of integers which contain the goals scored by Bruins
    and their opponents. Returns the number of games that the Bruins won
    """

    points = 0
    
    for i in range(len(bruins)):
        if bruins[i] > opponents[i]:
            points += 1

    return points

def print_results(bruins,opponents):
    """ takes two lists of integers containing the goals scored by the Bruins
    and their opponents. Prints the results of each game (no return value
    """

    for i in range(len(bruins)):
        if bruins[i] > opponents[i]:
            print('win', bruins[i], '-',opponents[i])
        elif opponents[i] > bruins[i]:
            print('loss',bruins[i], '-',opponents[i])
        else:
            print('tie',bruins[i], '-',opponents[i])
    

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('0) Input new goal lists')
    print('1) Get the latest score')
    print('2) Print the results')
    print('3) Find the number of wins')
    print('4) Find the max number of goals')
    
    ## Add any new menu options here.


    print('7) Quit')
    print()

def latest_score(bruins, opponents):
    """ returns the score of the latest (i.e., most recent) game
        inputs: bruins - a list of goals scored by the Bruins in a 
                  set of games
                opponents - a list of goals scored by their opponents
        We assume that both lists contain the same number of integers,
        and that they each contain at least one integer.
    """
    score = str(bruins[-1]) + '-' + str(opponents[-1])
    return score

## Add your helper functions for the remaining options below.
            

def main():
    """ the main user-interaction loop
    """
    bruins = []
    opponents = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            bruins = eval(input('Enter the Bruins list of goals: '))
            opponents = eval(input('Enter their opponents list of goals: '))
            if len(bruins) != len(opponents):
                print('The lists must have the same length.')
                print('Please select menu option 0 to try again.')
                bruins = []
                opponents = []
            
        elif choice == 7:
            break
        elif choice < 7 and len(bruins) == 0:
            print('You need to first enter the goal lists.')
            print('Please select menu option 0 to do so.')
        elif choice == 1:
            score = latest_score(bruins, opponents)
            print('The score of the latest game was', score)
        ## add code to process the other choices here

        elif choice == 2:
            results = print_results(bruins,opponents)
            print('The results are', results)


        else:
            print('Invalid choice. Please try again.')

    print('Goodbye!')
