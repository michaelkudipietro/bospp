import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers=list('0123456789') #create a list of digits 0 to 9
    random.shuffle(numbers) #shuffle them into random order

    #Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum+=str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with pico, fermi, bagels clues fora guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels' #There are no correct digits at all.
    else:
            #sort the clues in alphabetical order so their original order doesn't give info away
        clues.sort()
            #Make a single string from the lsit of string clues.
        return ' '.join(clues)
def main():
    print('''Bagels, a deductive logic game
 Credit to Al Sweigart al@inventwithpython.com
 
 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it it is. Here are some clues:
When I say:    That means:
 Pico          One digit is correct but in the wrong position.
 Fermi         One digit is correct and in the right position.
  Bagels       No digit is correct.

  For example, if the secret number the player needs to guess was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True: # Main game loop
        #this stores the secret number the player needs to guess:
        secretNum= getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses=1

        while numGuesses <=MAX_GUESSES:
            guess=''
            #Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{} '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses+=1

            if guess == secretNum:
                break
            if numGuesses >MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))
                
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')
    #End of main function

if __name__=='__main__':
    main()