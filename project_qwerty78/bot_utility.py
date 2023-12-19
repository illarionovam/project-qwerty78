from difflib import get_close_matches
from . import constants
from .exceptions import input_error
from .contact import Contact


def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        #TODO: add exceptions processing here
        except IndexError as e:
            return "Index out of range."
        except Exception as e:
            return e

    return inner


def process_command(command, args, book):
    
    
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

@input_error
def add_contact(args, address_book):
    name = args[0]
    phone = args[1] if len(args) > 1 and args[1] != '' else None
    birthday = args[2] if len(args) > 2 and args[2] != '' else None
    email = args[3] if len(args) > 3 and args[3] != '' else None
    address = args[4] if len(args) > 4 and args[4] != '' else None

    contact = Contact(name, phone, birthday, email, address)
    address_book.add_record(contact)
    return "Contact added"


@input_error
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


@input_error
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


@input_error
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


@input_error
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
