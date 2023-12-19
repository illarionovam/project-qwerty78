from difflib import get_close_matches
from . import constants
from .exceptions import wrap_exception
from .contact import Contact


def process_command(command, args, book):
    if command == constants.ADD_CONTACT_COMMAND:
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number (Enter - skip): ")
        birthday = input("Enter the contact's birthday (Enter - skip): ")
        email = input("Enter the contact's email (Enter - skip): ")
        address = input("Enter the contact's address (Enter - skip): ")
        print(add_contact([name, phone, birthday, email, address], book))
    elif command == constants.ADD_PHONE_COMMAND:
        print(add_phone(args, book))
    elif command == constants.ADD_BIRTHDAY_COMMAND:
        print(add_birthday(args, book))
    elif command == constants.ADD_EMAIL_COMMAND:
        print(add_email(args, book))
    elif command == constants.ADD_ADDRESS_COMMAND:
        print(add_address(args, book))
    else:
        return check_possible_commands(command)


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

@wrap_exception
def add_contact(args, address_book):
    name = args[0]
    phone = args[1] if len(args) > 1 and args[1] != '' else None
    birthday = args[2] if len(args) > 2 and args[2] != '' else None
    email = args[3] if len(args) > 3 and args[3] != '' else None
    address = args[4] if len(args) > 4 and args[4] != '' else None

    contact = Contact(name, phone, birthday, email, address)
    address_book.add_record(contact)
    return "Contact added"


@wrap_exception
def add_phone(args, address_book):
    if len(args) < 2:
        raise ValueError("Enter name and phone")
    name, phone = args
    contact = address_book.find(name)
    if contact:
        contact.phones.append(phone)
        return "Phone number added"
    else:
        raise KeyError


@wrap_exception
def add_address(args, address_book):
    if len(args) < 2:
        raise ValueError("Enter name and address")
    name, address = args
    contact = address_book.find(name)
    if contact:
        contact.address(address)
        return "Address added"
    else:
        raise KeyError


@wrap_exception
def add_birthday(args, address_book):
    if len(args) < 2:
        raise ValueError("Enter name and birthday date")
    name, birthday = args
    contact = address_book.find(name)
    if contact:
        contact.birthday(birthday)
        return "Birthday date added"
    else:
        raise KeyError


@wrap_exception
def add_email(args, address_book):
    if len(args) < 2:
        raise ValueError("Enter name and email")
    name, email = args
    contact = address_book.find(name)
    if contact:
        contact.email(email)
        return "Email added"
    else:
        raise KeyError
