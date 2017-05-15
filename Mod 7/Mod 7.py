########################################################################################################################
#   William Crabtree                                                                                                   #
#   11Apr17                                                                                                            #
#   Purpose: Create a contactbook. Allows for 3 total people.                                                          #
########################################################################################################################

import contact


def main():

    contacts = make_list()

    display_list(contacts)

# Gets data from users for 3 contact information points. Then puts that data into a list.


def make_list():

    # Create empty list
    contact_list = []

    # Get 3 contact information objects
    print("Enter contact information")
    for count in range(1, 4):

        # Get contact data
        print("Contact number:", count)
        name = input("Enter name: ")
        address = input("Enter address: ")
        age = input("Enter age: ")
        phone = input("Enter phone number: ")

        # Create new contact object in memory and assign it to the contact varible
        contacts = contact.Contact(name, address, age, phone)

        # Add the object to the list.
        contact_list.append(contacts)

    # Return the list.
    return contact_list


def display_list(contact_list):
    for item in contact_list:
        print(item.get_name())
        print(item.get_age())
        print(item.get_address())
        print(item.get_phone())
        print("*****")
# Call main function
main()
