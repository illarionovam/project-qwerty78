from difflib import get_close_matches
from . import exceptions
from .exceptions import wrap_exception
from . import constants
from . import contact


def process_command(command, args, book):
    if command == constants.ADD_CONTACT_COMMAND:
        if len(args) != 0:
            raise exceptions.IncorrectArgsException(
                "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_CONTACT_COMMAND])
        return entering_data(book)
    elif command == constants.ADD_PHONE_COMMAND:
        return add_phone(args, book)
    elif command == constants.ADD_BIRTHDAY_COMMAND:
        return add_birthday(args, book)
    elif command == constants.ADD_EMAIL_COMMAND:
        return add_email(args, book)
    elif command == constants.ADD_ADDRESS_COMMAND:
        return add_address(args, book)
    elif command == constants.SHOW_CONTACT_COMMAND:
        return show_contact(args, book)
    elif command in constants.EXIT_COMMANDS:
        return "Goodbye!"
    else:
        return check_possible_commands(command)
    

def check_input_for_contact(field, validated_constructor):
    try:
        validated_constructor(field)
        return True
    except exceptions.IncorrectArgsException as e:
        print(str(e))
        return False


def entering_data(book):
    while True:
        name = input("Enter the contact's name: ")
        if not name:
            print("Name cannot be empty. Please try again.")
        else:
            break
    while True:
        phone = input("Enter the contact's phone number (Enter - skip): ")
        if phone and not check_input_for_contact(phone, lambda field: contact.Phone(field)):
            continue
        else:
            break
    while True:
        birthday = input("Enter the contact's birthday (Enter - skip): ")
        if birthday and not check_input_for_contact(birthday, lambda field: contact.Birthday(field)):
            continue
        else:
            break
    while True:
        email = input("Enter the contact's email (Enter - skip): ")
        if email and not check_input_for_contact(email, lambda field: contact.Email(field)):
            continue
        else:
            break

    address = input("Enter the contact's address (Enter - skip): ")

    book.add_record(contact.Contact(name, phone, birthday, email, address))
    return "Contact added"


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
def show_contact(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SHOW_CONTACT_COMMAND])
    name = args[0]
    contact_var = book.find(name)
    return contact_var.printable_view()


@wrap_exception
def add_phone(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_PHONE_COMMAND])
    name, phone = args
    contact_var = book.find(name)
    return contact_var.add_phone(phone)
    

@wrap_exception
def add_address(args, book):
    if len(args) < 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_ADDRESS_COMMAND])
    name, address = args
    contact_var = book.find(name)
    return contact_var.add_address(address)


@wrap_exception
def add_birthday(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_BIRTHDAY_COMMAND])
    name, birthday = args
    contact_var = book.find(name)
    return contact_var.add_birthday(birthday)

    
@wrap_exception
def add_email(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_EMAIL_COMMAND])
    name, email = args
    contact_var = book.find(name)
    return contact_var.add_email(email)
        
