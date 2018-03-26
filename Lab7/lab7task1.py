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
    




    

    
