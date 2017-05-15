########################################################################################################################
#   William Crabtree                                                                                                   #
#   26Apr17                                                                                                            #
#   Purpose: The magic Triangle!                                                                                       #
########################################################################################################################

# Create list to show user where their input goes
usersNum = ["First Entry", "Second Entry", "Third Entry"]
genNum = ['Empty', 'Empty', 'Empty']


# Define how the triangle prints out


def triangle():

    # Basically, centering of the triangle so it always looks like a triangle
    fourth = '({})  [{}]  ({})'.format(genNum[0], usersNum[1], genNum[2])
    second = '[{}]'.format(usersNum[2]).center(int(len(fourth)/2), ' ')
    third = '[{}]'.format(usersNum[0]).center(int(len(fourth)/2), ' ')
    first = '({})'.format(genNum[1]).center(int(len(second) + len(third)), ' ')

    print(first)
    print(second, end="")
    print(third)
    print(fourth)


def UserLoop():
    # Loop three times
    for i in range(3):
        # Error Catch
        try:

            # Ask user for a number
            number = int(input("Enter a number between -40 and 40: "))

            # if users number is less than -40 or greater than 40, kick em out
            if -40 <= number <= 40:
                usersNum[i] = number
            else:
                print("Number was not in the correct range.")
                print(len(usersNum))
                exit()
        except ValueError:
            print("You did not enter a valid number.")
            exit()


def Math():
    # Get the total sum of numbers inputted and half it
    totalSum = int(sum(usersNum))/2

    # Subtract the sum from the opposite number and input that value into genNum
    for generatedNumber in range(3):
        genNum[generatedNumber] = totalSum - int(usersNum[generatedNumber])
print("Here is the triangle:")
triangle()
UserLoop()
Math()
print("Here is your final triangle.")
triangle()

