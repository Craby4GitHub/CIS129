########################################################################################################################
#   William Crabtree                                                                                                   #
#   27Feb17                                                                                                            #
#   Purpose: To figure out what the user will do for a week long vaction based on certain perferances                  #
#               and money avaiablity.                                                                                  #
########################################################################################################################

# Setting trip values

florence = 1500
staycation = 1400
camping = 240
visitingParents = 100
kayakinginLake = 100


print("Oh, you are going on a vacation? Lucky you!")
print("So we need to ask how much money you have to spend on this vacation")
totalMoney = int(input("What disposable income do you have for this trip? "))
print("Ok, now that we know how much you have, lets figure out what some of your perferences are.")

# Then we start asking questions

goingAbroad = input("What about going abroad? ")
if goingAbroad == "y":
    if florence <= totalMoney:
            print("Hey, you can go to Florence!")
            print("Going to Florence will cost a total of", florence)
    else:
            print("You can't go abroad because it will cost", florence)

drivingLongDistance = input("Are you willing or capable of driving a long distance? ")
if drivingLongDistance == "y":
        alone = input("Do you want to be alone? ")
        if alone == "y":
            if kayakinginLake <= totalMoney:
                print("You can go Kayaking in a remote lake.")
                print("That will only cost you gass money in the total of", kayakinginLake)
            else:
                print("You can't afford Kayaking in a lake becauseit costs", kayakinginLake)
            if camping <= totalMoney:
                print("You can go camping in a park.")
                print("That will cost you a total of", camping)
            else:
                print("You can't go camping because it costs", camping)
        if alone == "n":
            if visitingParents <= totalMoney:
                print("You can vist your parents, they miss you.")
                print("The only thing you need to buy is gas with a total cost of", visitingParents)
            else:
                print("You can't visit your parents because it costs", visitingParents)
elif drivingLongDistance == "n":
        if staycation <= totalMoney:
            print("Hey, you can do a Staycation at a nearby resort.")
            print("A Staycation will cost you a total of", staycation)
        else:
            print("You cant do a Staycation because it costs", staycation)
