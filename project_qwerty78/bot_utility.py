from difflib import get_close_matches

from . import constants
from . import exceptions
from .contact import Contact
from . import contact
from .exceptions import wrap_exception


def process_command(command, args, book):
    if command == constants.ADD_CONTACT_COMMAND:
        return entering_data(book)
    elif command == constants.ADD_PHONE_COMMAND:
        return Contact.add_phone(args, book)
    elif command == constants.ADD_BIRTHDAY_COMMAND:
        return Contact.add_birthday(args, book)
    elif command == constants.ADD_EMAIL_COMMAND:
        return Contact.add_email(args, book)
    elif command == constants.ADD_ADDRESS_COMMAND:
        return Contact.add_address(args, book)
    else:
        return check_possible_commands(command)


def entering_data(book):
    while True:
        name = input("Enter the contact's name: ")
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        phone = input("Enter the contact's phone number (Enter - skip): ")
        if phone and not contact.Phone.is_valid_phone(phone):
            print("The number must be 10 characters long. Please try again.")
            continue

        birthday = input("Enter the contact's birthday (Enter - skip): ")
        if birthday and not contact.Birthday.is_valid_date(birthday):
            print("The date of birth must be in the format DD.MM.YYYY and not later than today. Please try again.")
            continue

        email = input("Enter the contact's email (Enter - skip): ")
        if email and not contact.Email.is_valid_email(email):
            print("The email is not valid. Please try again.")
            continue

        address = input("Enter the contact's address (Enter - skip): ")

        return Contact.add_contact([name, phone, birthday, email, address], book)


def check_possible_commands(command):
    possible_commands = get_close_matches(command, constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys())
    for key in constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys():
        if command in key or key in command:
            if key not in possible_commands:
                possible_commands.append(key)

    return (constants.INVALID_COMMAND
            if len(possible_commands) == 0
            else (f"{constants.INVALID_COMMAND}\nMaybe, you wanted to run one of these commands?\n\n"
                  + "\n".join(constants.COMMAND_TO_COMMAND_FORMAT_MAP[x] for x in possible_commands)))



