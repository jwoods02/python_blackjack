# Blackjack
# Uses object oriented programming methodology
#NOTES
#Deck is fully simulated, cards will not come up twice but deck needs shuffling after each turn (use shuffle(deck))
#jack is 11, queen is 12, king is 13, Ace is 14 (Need to implement) 
#

import random
import time
from random import shuffle

def pause():
    """Defines a pause to help the game flow"""
    time.sleep(0.5)

def makeDeck():
    """Creates and shufles a deck of cards"""
    deck = []
    
    #Creates full deck of cards
    for suit in 'sdhc': 
        for value in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]:
            deck.append(str(value)+suit)
    
    #shuffles deck using imported shuffle
    shuffle(deck)
    
    return deck


def makePlayerHand():
    """Returns 2 cards from the deck"""
    hand = []
    for i in range(0, 2):
        hand.append(deck.pop()) #Takes bottom 2 cards from the deck list
    return hand


def makeDealerHand():
    """Returns ? placeholder for dealer and 2 cards from the deck"""
    hand = []
    hand.append("?") #Adds ? Placeholder to be replaced when player finishes hand
    for i in range(0, 2):
        hand.append(deck.pop()) #Takes bottom 2 cards from the deck list
    return hand


def Board():
    """Prints the hands of all players."""
    # ".join" function formats the list so it looks correct
    playerBoard = playerName + "'s Hand:  " + '     '.join(playerHand) + "     = "  + str(addCardValues(playerHand)) 
    
    if dealerHand[0] != "?": #if Dealer has not had a turn dealer's second hand it hidden? placeholder
            dealerBoard = "Dealer's Hand:  " + '     '.join(dealerHand) + "     = " + str(addCardValues(dealerHand))
    else:
        dealerBoard = "Dealer's Hand:  " + str(dealerHand[1]) + '     ' + str(dealerHand[0])
    pause()#A short pause to help game flow
    print(dealerBoard)
    print(playerBoard)


def playerBoard():
    """Prints the hand of the player."""
    # ".join" function formats the list so it looks correct
    playerBoard = playerName + "'s Hand:  " + '     '.join(playerHand) + "     = "  + str(addCardValues(playerHand)) 
    print(playerBoard)


def dealerBoard():
    """Prints the hands of the dealer."""
    # ".join" function formats the list so it looks correct
    if dealerHand[0] != "?": #if Dealer has not had a turn dealer's second hand it hidden? placeholder
            dealerBoard = "Dealer's Hand:  " + '     '.join(dealerHand) + "     = " + str(addCardValues(dealerHand))
    else:
        dealerBoard = "Dealer's Hand:  " + str(dealerHand[1]) + '     ' + str(dealerHand[0])
    pause()#A short pause to help game flow
    print(dealerBoard)

def addCardValues(player):
    """Returns the values of all cards in any hand added together"""
    additionHand = player#detects list variable for the selected players hand
    totalValue = 0
    currentValue = 0
    aceNumber = 0
    for i in range(0, len(additionHand)): # for every card in the selected players hand
        if additionHand[i] == "?":#if the entry is the dealers ? then skip the loop
            currentValue = 0
            continue
        else:
            currentCard = additionHand[i]#selects individual card
            currentValue = currentCard[:-1]#gets rid of suit for selected card, just card value
            if currentValue in ("J", "Q", "K"): #if picutre card (excluding ace)
                currentValue = 10 #set value to 10
            elif currentValue == "A": #if card is ace
                currentValue = 1 #set ace to equal 1 (logic applied at end of hand)
                aceNumber += 1

            totalValue += int(currentValue)

        #ENDFOR

    #Ace logic
    if aceNumber > 0: #if any card is an ace
        for i in range(0, aceNumber): # for all aces
            if totalValue < 12: #if adding value of ace does not bust
                totalValue += 10 #add 10 (the 1 is already added)

    return totalValue


def playerTurn():
    """"Asks the player if they want to hit or stand and calls the appropiate function"""
    userAction = input("Would you like to hit or stand? ").lower() #User input (.lower() function used so input not case sensitive)
    if userAction.startswith("h"):
        hit(playerHand)
    elif userAction.startswith("s"):
        return "break"#turn ends at break
    else:
        print("Input not valid please enter a string starting with h to hit or s to stand")
        
    

def hit(hand):
    """adds a crad from the deck to 'hand'"""
    hand.append(deck.pop())
    
def isBust(hand):
    """Uses addCardValues to determine if a player has gone bust"""
    if addCardValues(hand) > 21:
        return True
    else:
        return False


def dealerTurn():
    """Dealer takes their turn"""
    if addCardValues(dealerHand) < 17:
        hit(dealerHand)
    else:
        return False


def playAgain():
    userAgainInput = input(playerName + " would you like to play again? (Y/N)").lower() #user input (.lower() function used so input not case sensitive)

    if userAgainInput.startswith("n"):
        return False
    
    
def whoWins():
    """Determines who wins, adds a point to their score and prints the winner, or prints draw"""

    #Tell Python dealerScore and playerScore refer to global variables
    global dealerScore
    global playerScore
    
    if isBust(playerHand) == True:#if player is bust
        dealerScore += 1 #Adds a point to the dealer
        print("You went bust! The dealer gets a point.")

    elif isBust(dealerHand) == True:#if dealer is bust
        playerScore += 1 #Adds a point to the player
        print("The dealer went bust! You get a point.")

    elif addCardValues(playerHand) > addCardValues(dealerHand): #if the players cards add up to more than dealers
        playerScore += 1 #Adds a point to the player
        print("Well done " + playerName + "you win!")

    elif addCardValues(dealerHand) > addCardValues(playerHand): #if the dealers cards add up to more than players
        dealerScore += 1 #Adds a point to the dealer
        print("Unlucky, the dealer wins.")

    else:
        print("The game is tied! Nobody gets a point this time...")


def scoreBoard():
    print(playerName + ":" , str(playerScore), "Dealer:", str(dealerScore))




"""START OF MAIN GAME"""

#Sets scores for the game

playerScore = 0

dealerScore = 0

#Asks for Player's name
playerName = input("Please enter your name: ")

pause()

print("Blackjack:")

pause()

print("The aim of the  game is for the value of your cards to equal 21")

pause()

while True:

    #set up deck and hands
    deck = makeDeck()

    playerHand = makePlayerHand()

    dealerHand = makeDealerHand()

    Board()#show starting hands

    pause()#A short pause to help game flow

    while isBust(playerHand) == False:#if player busts turn ends else player gets more turns

        pause()
        
        if playerTurn() == "break":#player takes turn, if statement evaluates to true if player chooses to stand
            break #breaks if player stands
        
        playerBoard()#shows the players hand after each turn

    #END PLAYER HAND

    pause()

    print("Your turn is finished")

    pause()

    time.sleep(1)#Extended pause
        
    if isBust(playerHand) == True:#if player is bust
        pass
        #Skips to whoWins() as dealer does not take turn

    else:

        print("The dealer will now take his turn")

        pause()
        
        dealerHand.remove("?") #delete the placeholder card
        
        dealerBoard() #print the board with dealer's card revealed
        
        while dealerTurn() != False:#Performs the dealers turn, dealerTurn() returns false when bust or over 17.
            time.sleep(2)#2 second gap between each turn for game flow
            dealerBoard()#Prints booard after each dealer turn
        
        #END DEALER HAND

    time.sleep(2)#Extended pause
 
    whoWins()#Determines and prints who wins.

    pause()

    scoreBoard()#prints scores

    pause()
    
    if playAgain() == False:
        break



    

