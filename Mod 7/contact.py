# The Contact class holds data about a contact.
class Contact:

    # The __init__ method initializes the attributes.

    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # The set_name method accepts an argument for the contacts' name.

    def set_name(self, name):
        self.__name = name

    # The set_address method accepts an argument for the contacts' address.

    def set_address(self, address):
        self.__address = address

    # The set_age method accepts an argument for the contacts' age

    def set_age(self, age):
        self.__age = age

    # The set_phone method accepts an argument for the contacts phone number

    def set_phone(self, phone):
        self.__phone = phone

    # The get_name method returns the contacts' name.

    def get_name(self):
        return self.__name

    # The get_model method returns the contacts' age

    def get_age(self):
        return self.__age

    # The get_phone method returns the contacts' phone number

    def get_phone(self):
        return self.__phone

    # The get_adddress method returns the contacts' address

    def get_address(self):
        return self.__address
