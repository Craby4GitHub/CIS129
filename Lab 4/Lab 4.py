#! python3

########################################################################################################################
#   Slot Machine                                                                                                       #
#   Author: William Crabtree                                                                                           #
#   4April17                                                                                                           #
#   Purpose: Ask user for tenant names and then print out rent slip for each month.                                    #
########################################################################################################################


def main():
    # Set rent amount due
    rentDue = [0, 300, 400, 250, 500, 1000]

    # Create empty tenant list
    tenantNames = [0]

    # Ask user for tenant names
    for apartmentNumber in range(1, 6):
        print("Apartment Number:", apartmentNumber)
        tenantName = input("What is the name of the tenant in apartment ")

        # add names to the list
        tenantNames.append(tenantName)

    # Create month list
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Start loop counting months
    outerCount = 0
    while outerCount <= 11:

        # Index current month
        currentMonth = months[outerCount]

        innerCount = 1
        while innerCount <= 5:
            print("Rent for", tenantNames[innerCount], "in apt", innerCount, "is", rentDue[innerCount], "this", currentMonth)
            innerCount += 1

        outerCount += 1

main()
