'''Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game of blackjack, also known as 21.
This unmodified version does not have splitting or insurance.
More info at https://en.wikipedia.org/wiki/Blackjack
'''

import random, sys

#set up constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print('''Blackjack, by Al Sweigart
          Rules:
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.
          ''')
    money=5000
    while True: #main game loop
        #check if player has run out of money
        if money <=0:
            print('''You're broke!
                  Good thing we weren't playing with real money
                  Thanks for playing!
                  ''')
            sys.exit()

        #let the player enter their bet for this round

        
        print('Money:', money)
        bet=getBet(money)

        #Give the dealer and player two cards from the deck each
        deck=getDeck()
        dealerHand=[deck.pop(),deck.pop()]
        playerHand=[deck.pop(),deck.pop()]

        #handle player actions
        print('Bet:', bet)
        while True: #Keep looping until player stands or busts
            displayHands(playerHand,dealerHand,False)
            print()

            #Check if the player has bust
            if getHandValue(playerHand)>21
                break
            
            #get player's move, either H, S, or D
            move = getMove(playerHand, money - bet)

            #Handle the player actions:
            if move == 'D':
                #Player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet,(money-bet)))
                bet+=additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:',bet)

            if move in ('H','D')
                #Hit/doubling down, takes another card
                newCard=deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)

                if getHandValue(playerHand)>21:
                    #The player has busted:
                    continue
            if move in ('S','D'):
                #Stand/doubling down stops the player's turn.
                break

            #Handle the dealer's actions
        if getHandValue(playerHand) <=21:
            while getHandValue(playerHand) <17:
                #The dealer hit:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) > 21:
                    break: #dealer has busted
                input('Press Enter to continue')
                print('\n\n')

                #Show the final hands:
                displayHands(playerHand, dealerHand, True)

                playerValue = getHandValue(playerHand)
                dealerValue = getHandValue(dealerHand)
                #handle whether the player won, lost, or tied
                if  dealerValue > 21:
                    print('Dealer busts! You win ${}!'.format(bet))
                    money+=bet
                elif(playerValue > 21) or (playerValue < dealerValue):
                    print('You lost!')
                    money -=bet
                elif(playerValue > dealerValue):
                    print('You won ${}!'.format(bet))
                    money+=bet
                elif playerValue == dealerValue:
                    print('It\s a tie, your bet is returned to you.')

                input('Press Enter to continue...')
                print('\n\n')

def getBet(maxBet):
    '''Ask the player how much they want to bet for this round.'''
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet =='QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue #if player didn't enter a number, ask again.

        bet=int(bet)
        if 1 <= bet <= maxBet:
            return bet #Player entered a valid bet
def getDeck():
'''Return a list of (rank,suit) tuples for all 52 cards'''
deck = []
for suit in (HEARTS,DIAMONDS, SPADES, CLUBS)
    for rank in range(2,11):
        deck.append((str(rank),suit))#Add the numbered cards.
    for rank in ('J','Q','K','A'):
        deck.append((rank,suit)) #Add the numbered cards
random.shuffle(deck)
return deck

def displayHands(playerHand,dealerHand,showDealerHand):
    '''Show the player's and dealers cards. Hide the dealer's first card if showDealerHand is False'''
    print()
    if showDealerHand():
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:',getHandValue(playerHand))
    displayCards(playerHand)


    #Start here after merging with github main branch - use git from terminal going forward
