########################################################################################################################
#   Slot Machine                                                                                                       #
#   Author: William Crabtree                                                                                           #
#   2March17                                                                                                           #
#   Purpose: To pick random word then multipply users bet based on the random values picked                            #
########################################################################################################################
import random
########################################################################################################################
# Sets the words and randomly picks one
########################################################################################################################
values = "Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"
rPick1 = random.choice(values)
rPick2 = random.choice(values)
rPick3 = random.choice(values)
########################################################################################################################
# Asking for user bet and doing some error handling                                                                    #
########################################################################################################################
try:
    userBet = float(input("Enter your bet amount: "))
except ValueError:
    print("This isnt a free slot machine, get outta here!")
    exit()
########################################################################################################################
# Setting minimum bet                                                                                                  #
########################################################################################################################
if userBet < .25:
    print("Sorry, that is not enough money to bet. The minimum is 25 cents.")
    exit()
else:
    print("Your random words are", rPick1, rPick2, rPick3)
########################################################################################################################
# Verifies picks agaisnt each other                                                                                    #
########################################################################################################################
wonBet = 0
if rPick1 and rPick2 and rPick3 == rPick1 and rPick2 and rPick3:
    wonBet = 3
if rPick1 and rPick2 == rPick1 and rPick2:
    wonBet = 2
if rPick1 and rPick3 == rPick1 and rPick3:
    wonBet = 2
if rPick2 and rPick3 == rPick2 and rPick3:
    wonBet = 2
########################################################################################################################
# Define currency, to find out whether  to use bucks or cents                                                          #
########################################################################################################################


def currency():
    if totalWon >= 1:
        print("You won", totalWon, "bucks!")
    else:
        print("You won", totalWon, "cents!")
########################################################################################################################
# Informs user how much they have won                                                                                  #
########################################################################################################################
if wonBet == 3:
    print("You won 3x your bet!")
    totalWon = userBet * wonBet
    currency()
if wonBet == 2:
    print("You won 2x your bet!")
    totalWon = userBet * wonBet
    currency()
if wonBet == 0:
    print("Sorry, you lost and you get $0 :[")
