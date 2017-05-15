pickMonth = int(input("Pick a number of a month. "))


#if pickMonth == 1:
#    print("Your month is January.")
#elif pickMonth == 2:
#    print("Your month is Febuary.")
#elif pickMonth == 3:
#    print("Your month is March.")
#elif pickMonth == 4:
#    print("Your month is April.")
#else:
#    print("Your month is not avalible.")


def switch(inval):
    value = {
        1: "January",
        2: "Febuary",
        3: "March"
    }
    return value.get(inval, "invalid")
stringVal = switch(pickMonth)
print("Your month is ", stringVal)
