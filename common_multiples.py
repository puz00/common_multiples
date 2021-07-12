#!/usr/bin/python3
# finding common multiples
# by puz00
# this program allows a user to find the common multiples of any number of times-tables
# they control how many times-tables and which ones, too

def get_common_multiples(length):
    # checks if each number in the first times-table is in the subsequent ones
    # we start by assuming that it is a common multiple but mark it as False
    # if it is not in any of the subsequent times-tables
    for i in range(length):
        common = True
        number = multiples[0][i]
        for j in range(1, len(multiples)):
            if number not in multiples[j]:
                common = False
        if common == True:
            common_multiples.append(number)

# main
common_multiples = []

# get how many multiples of the numbers the user wants to check
# exception handling used to force an integer as input
got_length = False
while got_length == False:
    try:
        length = int(input('How many multiples would you like for each number? '))
        got_length = True
    except:
        print('\nYou need to input a number such as 5, 10, 12 etc...\n')

# get how many times-tables the user wants to use
# exception handling used to force an integer as input
got_tables = False
while got_tables == False:
    try:
        tables = int(input('\nHow many times-tables do you want to use? '))
        got_tables = True
    except:
        print('\nYou need to input a number such as 2, 5 or 8...\n')

# create a list of the correct length to store the products of the times-tables in later
multiples = [0] * tables

# the user inputs the times-tables they would like to use
# the products of the times-tables are worked out and stored in a 2D array (multiples)
for i in range(tables):
    table = int(input('\nEnter the times-table: '))
    multiples[i] = [x * table for x in range(1, length+1)]

# get_common_multiples is called to work out the common multiples
get_common_multiples(length)

# the information needed by the user is generated from the list of common multiples
# the computer works out how many common multiples there are (cm);
# the greatest common multiple (gcm);
# and the lowest common multiple (lcm);
# error handling deals with the possibility that there are no common multiples
try:
    cm = len(common_multiples)
    gcm = max(common_multiples)
    lcm = min(common_multiples)
except:
    print('\nNo common multiples found')
    print('\nThankyou...goodbye!')
    exit()

# the information is given to the user
print('\nThere are: {} common multiples'.format(cm))
print('\nThe greatest common multiple is: {}'.format(gcm))
print('\nThe lowest common multiple is: {}'.format(lcm))

# the user is given the option to see all of the common multiples
show = input('\nDo you want to see all of the common multiples? (y = yes / n = no): ').lower()
if show.startswith('y'):
    print('\n{}'.format(common_multiples))
print('\nThankyou...goodbye!')