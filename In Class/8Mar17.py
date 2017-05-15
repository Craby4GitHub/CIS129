#
#
# Find Prime Number

#
#


def main():
    try:
        inputnum = int(input("Enter a positive prime number: "))
    except:
        print("Intergers only please.")

    while inputnum > 1:
        remainder = 0
        maxrange = int(inputnum / 2) + 1
        for counter in range(2, maxrange):
            remainder = inputnum % counter
            if remainder == 0:
                print(str(inputnum), "is not prime.")
                break
        if remainder != 0:
            print(str(inputnum), "is prime.")
        try:
            inputnum = int(input("Enter a positive prime number: "))
        except:
            print("Intergers only please.")
            exit()

main()

