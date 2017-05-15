########################################################################################################################
#   William Crabtree, Greg Wagner                                                                                      #
#   7Mar17                                                                                                             #
#   Purpose: To figure out if a cookie contains gluten and if it is, judge it harshly.                                 #
########################################################################################################################

########################################################################################################################
#   Prompt the user for the cookie name and read the input                                                             #
#   The name will be used when prompting for more information                                                          #
########################################################################################################################
cookieName = input("what is the name of the cookie? ")

########################################################################################################################
#   Prompt the user if the cookie contains chocolate, peanut butter and/or gluten.                                     #
########################################################################################################################
containsChocolate = input("Does "+cookieName+" contain chocolate? (Y or N) ")
containsPeanutbutter = input("Does "+cookieName+" contain peanut butter? (Y or N) ")
containsGluten = input("Does "+cookieName+" contain gluten? (Y or N) ")

########################################################################################################################
# Compare the value to "Y"                                                                                             #
########################################################################################################################
if containsChocolate == "Y" or containsPeanutbutter == "Y" and containsGluten == "N":
    print(cookieName, "is a good cookie! ")
else:
    print(cookieName, "is a bad cookie.")
