########################################################################################################################
#   William Crabtree                                                                                                   #
#   24Apr17                                                                                                            #
#   Purpose: Dictionary that contain rm #, teacher and time. Ask user for course #, display releveant info            #
########################################################################################################################


def main():
    # Create Course Room Dictionary
    courseroom = {'CS101': "3004", 'CS102': "4501", 'CS103': "6755", 'NT110': "1244", 'CM241': "1411"}

    # Create Course Teacher Dictionary
    courseteacher = {'CS101': "Hayes", 'CS102': "Alvardo", 'CS103': "Rich", 'NT110': "Burke", 'CM241': "Lee"}

    # Create Course Time Dictionary
    coursetime = {'CS101': "8:00AM", 'CS102': "9:00AM", 'CS103': "10:00AM", 'NT110': "11:00AM", 'CM241': "1:00PM"}

    # Ask for course number
    userinput = input('What is the course number?').upper()

    # Display results
    print("The room for " + userinput, "is " + courseroom[userinput]+".")
    print("The teacher for " + userinput, "is " + courseteacher[userinput]+".")
    print("The time for " + userinput, "is " + coursetime[userinput]+".")

# Run
main()
