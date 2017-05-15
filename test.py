class IdentityCard:

    num_of_contacts = 0

#       Constructor

    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = ""
        self.phone = ""

        IdentityCard.num_of_contacts += 1

#       Modifiers
    def printdata(self):
        print("Name: " + self.name)
        print("Address: " + str(self.address))
        print("Age: " + self.age)
        print("Phone: " + self.phone)


#       Accessors AKA getters and setters
    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age

    def setphone(self, phone):
        self.phone = phone

idCard = IdentityCard()

idCard.name = input("test")
idCard.address = input("another test")
idCard.phone = input("I dunno")
idCard.printdata()
print(idCard.getaddress())
print("There are", idCard.num_of_contacts, "contacts.")

'''

idCard.setname(name)
idCard.setaddress(address)
idCard.setage(age)
idCard.setphone(phone)

frName = input("Enter your name: ")
frAddress = input("Enter your adress: ")
frAge = input("Enter your age: ")
frPhone = input("Enter your phone number: ")

idCard.setname(frName)
idCard.setaddress(frAddress)
idCard.setage(frAge)
idCard.setphone(frPhone)

faName = input("Enter your name: ")
faAddress = input("Enter your adress: ")
faAge = input("Enter your age: ")
faPhone = input("Enter your phone number: ")

idCard.setname(faName)
idCard.setaddress(faAddress)
idCard.setage(faAge)
idCard.setphone(faPhone)

print(IdentityCard.getaddress(frAddress))

#idCard.printdata()
'''