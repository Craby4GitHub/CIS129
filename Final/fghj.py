userResponse = []


def getInput():

    while len(userResponse) <= 2:
            try:
                userInput = int(input("input number: "))

                if -40 <= userInput <= 40:
                    userResponse.append(userInput)

                else:
                    print("Only integer numbers -40 to 40!")
            except ValueError:
                print("Integers only!")
                continue
getInput()