import random

DIGITS_NUM = 11 #this is the number of digits for guessing
MAX_NUMBER_ATTEMPTS = 10 #this is the number of attempts to guess the number

def main():
    print(''' Bagels, a deductive logic game.
    by Al Sweigart al@inventwithpython.com
    
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
      Pico          One digit is correct but in the wrong position
      Fermi         One digit is correct and in the right position
      Bagels        No digit is correct '''.format(DIGITS_NUM))

    while True: #Main game loop
        # This socres the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have though up a number.')
        print(' You have {} guesses to get it.'.format(MAX_NUMBER_ATTEMPTS))

        numGuesses = 1
        while numGuesses <= MAX_NUMBER_ATTEMPTS:
            guess = ''
            #keep looping until they enter a valid guess:
            while len(guess) != DIGITS_NUM or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct, so break out of this loop
            if numGuesses > MAX_NUMBER_ATTEMPTS:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        #Ask the player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thank you for Playing')

def getSecretNum():
    """Returns a string made of a DIGITS_NUM unique random digits."""
    numbers = list('0123456789') # create a list of digits 0 to 9
    random.shuffle(numbers) # shuffles the number into a random order.

    #get the first DIGITS_NUM digits in the list for the secret number:
    secretNum = ''
    for i in range(DIGITS_NUM):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit in the wrong place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()