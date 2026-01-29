
def average_age():

    '''Average Age Program
    By Grace LeVoir
    1 - 29 - 26'''

    # Get User Input

    age_1 = int(input('Enter the age of a friend: '))
    age_2 = int(input('Enter the age of another friend: '))
    age_3 = int(input('Enter the age of another friend again: '))
    age_4 = int(input('Enter the age of yet another friend: '))
    age_5 = int(input('Enter the age of yet another friend again: '))

    # Sum ages

    sum = age_1 + age_2 + age_3 + age_4 + age_5

    # Average the ages

    average = sum / 5

    # Print the results

    print()
    print(f'The average age of these five friends is {average}.')

# Line which calls the above function.
average_age()