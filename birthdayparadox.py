import datetime, random
from collections import Counter

def getBirthdays(numberOfBirthdays):
        """Returns a list of number random date objects for birthdays."""
        birthdays = []
        for i in range(numberOfBirthdays):
            #year is irrelevant, as long as all birthdays have the same year
            startOfYear=datetime.date(2001,1,1)

            #Get a random day into the year:
            randomNumberOfDays=datetime.timedelta(random.randint(0,364))
            birthday= startOfYear + randomNumberOfDays
            birthdays.append(birthday)
        return birthdays
def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list"""
    counts = Counter(birthdays)
    for date, count in counts.items():
        if count > 1:
            return date
    return None
            
#Display intro
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
      
      The Birthday Paradox shows us that in a group of N people, the odds
      that two of them have matching birthdays is surprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random simulations)
      to explore this concept.

      (it's actually not a paradox, just a surprising result)
      ''')

#set up tuple with month names

MONTHS=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
while True:

    while True: #keep asking until the user enters a valid amount.
        print('How many birthdays shall I generate (Max 100)')
        response = input('> ')
        if response.isdecimal() and (0<int(response) <=100):
                numBDays=int(response)
                break #User has entered a valid amount
    print()



    #Generate and display the birthdays:

    print('Here are', numBDays,'birthdays:\n')
    birthdays=getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        monthName=MONTHS[birthday.month -1]
        dateText= f'{monthName} {birthday.day}'
        if i != 0:
            print(', ',end='')
            dateText='{} {}'.format(monthName,birthday.day)
        print(dateText, end='')
    print()
    print()

    #Determine if any of the birthdays match
    match=getMatch(birthdays)

    #Display the results:
    print('In this simulation,', end='')
    if match != None:
        monthName=MONTHS[match.month - 1]
        dateText = '{}{}'.format(monthName, match.day)
        print('multiple people have birthdays on', dateText)
    else:
        print('there are no matching birthdays.')
    print()

    #Run through 100,000 simulations
    print('Generating',numBDays,'random birthdays 100,000 times...')
    input('Press Enter to begin...')

    print('Let\'s run another 100,000 simulations.')
    simMatch=0 #How many simulations have matching birthdays in them
    for i in range(100_000):
        #Report the progress every 10,000 simulations
        if i%10_000==0:
            print(i,'simulations run...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1
    print('100,000 simulations run.')

    #display sim results
    probability = round(simMatch/100_000*100,2)
    print('Out of 100,000 simulations of',numBDays,'people, there was a')
    print('matching birthday in that group', simMatch,'times. This means')
    print('that', numBDays, 'people have a',probability,'% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')
    again=input("Do you want to run another simulation? (y/n): ").lower()
    if again !='y':
        print('Thanks for your time!')
        break