########################################################################################################################
#   William Crabtree, Greg Wagner                                                                                      #
#   30Mar17                                                                                                            #
#   Purpose: Compare students answers to an answer file, the inform user if they passed or failed.                     #
########################################################################################################################

#   number you are trying to match
MAGIC_NUMBER = 9

#   set count
count = 0

#   read in name
sName = input("What is your name? ")

#   start loop
while count <= 3:

    #   read in number
    try:
        numberGuessed = int(input(sName + ", pick a number between 0 and 10. "))
    except ValueError:
        print("Make sure your guess is a numerical number between 0 and 10.")
        exit()
    if numberGuessed < 0 or numberGuessed > 10:
        print("Sorry, that number is not in the correct range.")
        break
    #   compare number guessed to magic number
    if numberGuessed == MAGIC_NUMBER:
        print("After", +count, "guesses, you got it right!")
        break
    if numberGuessed < MAGIC_NUMBER:
        print(sName + ", you picked " + str(numberGuessed), "and it is too low.")
        count += 1
    else:
        print(sName + ", you picked " + str(numberGuessed), "and it is too high.")
        count += 1
print("Thats all the guesses you get.")
