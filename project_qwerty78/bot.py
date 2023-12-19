from .bot_utility import process_command
from .constants import INVALID_COMMAND, EXIT_COMMANDS


import bot_utility
from .address_book import AddressBook

CLOSE_COMMAND = "close"
EXIT_COMMAND = "exit"
ADD_CONTACT_COMMAND = "add-contact"
ADD_PHONE_COMMAND = "add-phone"
ADD_BIRTHDAY_COMMAND = "add-birthday"
ADD_ADDRESS_COMMAND = "add-address"
ADD_EMAIL_COMMAND = "add-email"


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    # read from file
    address_book = AddressBook()
    print("Welcome to the assistant bot!")

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
            #process command

            if command in ['close', 'exit'] and len(args) == 0:
                break
            elif command == ADD_CONTACT_COMMAND:
                name = input("Enter the contact's name: ")
                phone = input("Enter the contact's phone number (Enter - skip): ")
                birthday = input("Enter the contact's birthday (Enter - skip): ")
                email = input("Enter the contact's email (Enter - skip): ")
                address = input("Enter the contact's address (Enter - skip): ")
                print(bot_utility.add_contact([name, phone, birthday, email, address], address_book))
            elif command == "change":
                print(bot_utility.change_contact(args, address_book))
            elif command == ADD_PHONE_COMMAND:
                print(bot_utility.add_phone(args, address_book))
            elif command == ADD_BIRTHDAY_COMMAND:
                print(bot_utility.add_birthday(args, address_book))
            elif command == ADD_EMAIL_COMMAND:
                print(bot_utility.add_email(args, address_book))
            elif command == ADD_ADDRESS_COMMAND:
                print(bot_utility.add_address(args, address_book))
        except:
            print("Invalid command.")
    
    #write to file

    # write to file


if __name__ == "__main__":
    main()
