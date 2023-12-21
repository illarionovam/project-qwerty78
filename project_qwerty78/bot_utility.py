from difflib import get_close_matches
from . import exceptions
from .decorators import wrap_exception
from . import constants
from . import contact
from . import note
from .birthday_utility import get_birthdays_per_days_range
from rich.table import Table
from rich.style import Style
from .easter_eggs import EasterEgg


def process_command(command, args, book):
    if command == constants.ADD_CONTACT_COMMAND:
        return add_contact(args, book)
    elif command == constants.ADD_PHONE_COMMAND:
        return add_phone(args, book)
    elif command == constants.SET_NAME_COMMAND:
        return set_name(args, book)
    elif command == constants.SET_BIRTHDAY_COMMAND:
        return set_birthday(args, book)
    elif command == constants.SET_EMAIL_COMMAND:
        return set_email(args, book)
    elif command == constants.SET_ADDRESS_COMMAND:
        return set_address(args, book)
    elif command == constants.SHOW_CONTACT_COMMAND:
        return show_contact(args, book)
    elif command == constants.REMOVE_CONTACT_COMMAND:
        return remove_contact(args, book)
    elif command == constants.REMOVE_EMAIL_COMMAND:
        return remove_email(args, book)
    elif command == constants.REMOVE_ADDRESS_COMMAND:
        return remove_address(args, book)
    elif command == constants.REMOVE_BIRTHDAY_COMMAND:
        return remove_birthday(args, book)
    elif command == constants.REMOVE_PHONES_COMMAND:
        return remove_phones(args, book)
    elif command == constants.REMOVE_PHONE_COMMAND:
        return remove_phone(args, book)
    elif command == constants.ALL_CONTACTS_COMMAND:
        return all_contacts(args, book)
    elif command == constants.ALL_NOTES_COMMAND:
        return all_notes(args, book)
    elif command == constants.SHOW_BIRTHDAY_COMMAND:
        return show_birthday(args, book)
    elif command == constants.SHOW_NOTE_COMMAND:
        return show_note(args, book)
    elif command == constants.ADD_NOTE_COMMAND:
        return add_note(args, book)
    elif command == constants.REMOVE_NOTE_COMMAND:
        return remove_note(args, book)
    elif command == constants.SET_TITLE_COMMAND:
        return set_title(args, book)
    elif command == constants.REMOVE_TITLE_COMMAND:
        return remove_title(args, book)
    elif command == constants.SET_CONTENT_COMMAND:
        return set_content(args, book)
    elif command == constants.ADD_TAG_COMMAND:
        return add_tag_to_note(args, book)
    elif command == constants.REMOVE_TAG_COMMAND:
        return remove_tag_from_note(args, book)
    elif command == constants.REMOVE_TAGS_COMMAND:
        return remove_all_tags_from_note(args, book)
    elif command == constants.HELP_COMMAND:
        return help_menu()
    elif command in constants.EXIT_COMMANDS:
        return "Goodbye!"
    else:
        return check_possible_commands(command)


def help_menu():
    table = Table(show_lines=True)

    header_style = Style(bgcolor="rgb(88,205,54)")
    table_style = Style(bgcolor="rgb(211,211,211)")
    for column in ["Command", "Command Format", "Does"]:
        if column == "Command Format":
            table.add_column(column, header_style=header_style, style=header_style)
        else:
            table.add_column(column, header_style=header_style, style=table_style)

    for command, help_text in constants.COMMAND_TO_HELP_TEXT_MAP.items():
        table.add_row(command, constants.COMMAND_TO_COMMAND_FORMAT_MAP[command], help_text)

    return table


def check_input_for_record(field, validated_constructor):
    try:
        validated_constructor(field)
        return True
    except exceptions.IncorrectArgsException as e:
        print(str(e))
        return False


@wrap_exception
def add_note(args, book):
    if len(args) != 0:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_NOTE_COMMAND])

    while True:
        title = input("Enter the note's title (Enter - skip): ").strip()
        if title and not check_input_for_record(title, lambda field: note.Title(field)):
            continue
        else:
            break

    while True:
        content = input("Enter the note's content: ").strip()
        if not check_input_for_record(content, lambda field: note.Content(field)):
            continue
        else:
            break

    EasterEgg.ENABLED = False
    book.add_note(note.Note(content, title))
    EasterEgg.ENABLED = True
    return "Note added"


@wrap_exception
def set_title(args, book):
    if len(args) < 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_TITLE_COMMAND])
    index = book.prepare_index(args[0]) 
    new_title = " ".join(args[1:])
    note_var = book.find_note(index)
    return note_var.set_title(new_title)


@wrap_exception
def set_content(args, book):
    if len(args) < 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_CONTENT_COMMAND])
    index = book.prepare_index(args[0])  
    new_content = " ".join(args[1:])
    note_var = book.find_note(index)
    return note_var.set_content(new_content)


@wrap_exception
def remove_note(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_NOTE_COMMAND])

    index = book.prepare_index(args[0])
    return book.remove_note(index)


@wrap_exception
def add_contact(args, book):
    if len(args) != 0:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_CONTACT_COMMAND])

    while True:
        name = input("Enter the contact's name: ").strip()
        if not check_input_for_record(name, lambda field: contact.Name(field)):
            continue
        else:
            break

    try:
        book.find_contact(name)
        return f"Contact with {name} already exists. Please, edit the existing one."
    except exceptions.NoRecordException:
        pass

    while True:
        phone = input("Enter the contact's phone (Enter - skip): ").strip()
        if phone and not check_input_for_record(phone, lambda field: contact.Phone(field)):
            continue
        else:
            break
    while True:
        birthday = input("Enter the contact's birthday (Enter - skip): ").strip()
        if birthday and not check_input_for_record(birthday, lambda field: contact.Birthday(field)):
            continue
        else:
            break
    while True:
        email = input("Enter the contact's email (Enter - skip): ").strip()
        if email and not check_input_for_record(email, lambda field: contact.Email(field)):
            continue
        else:
            break

    address = input("Enter the contact's address (Enter - skip): ").strip()

    EasterEgg.ENABLED = False
    book.add_contact(contact.Contact(name, phone, birthday, email, address))
    EasterEgg.ENABLED = True
    return "Contact added"


def check_possible_commands(command):
    possible_commands = get_close_matches(command, constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys())
    for key in constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys():
        if command in key or key in command:
            if key not in possible_commands:
                possible_commands.append(key)

    table = Table(box=None, show_header=False)
    table.add_column(style=Style(bgcolor="rgb(88,205,54)"))
    table.add_row(constants.INVALID_COMMAND, style=Style(bgcolor=constants.RED_COLOR))

    if len(possible_commands) != 0:
        table.add_row("Maybe, you wanted to run one of these commands?\n", style=Style(bgcolor="rgb(255,255,255)"))
        for command in possible_commands:
            table.add_row(constants.COMMAND_TO_COMMAND_FORMAT_MAP[command])

    return table


@wrap_exception
def show_contact(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SHOW_CONTACT_COMMAND])
    search_value = args[0]
    return book.show_contacts(book.find_contact_by_search_value(search_value))


@wrap_exception
def remove_phones(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_PHONES_COMMAND])
    name = args[0]
    contact_var = book.find_contact(name)
    return contact_var.remove_phones()


@wrap_exception
def remove_phone(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_PHONE_COMMAND])
    name, phone = args
    contact_var = book.find_contact(name)
    return contact_var.remove_phone(phone)


@wrap_exception
def remove_email(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_EMAIL_COMMAND])
    name = args[0]
    contact_var = book.find_contact(name)
    return contact_var.remove_email()


@wrap_exception
def remove_title(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_TITLE_COMMAND])
    index = book.prepare_index(args[0])
    note_var = book.find_note(index)
    return note_var.remove_title()


@wrap_exception
def remove_address(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[
                constants.REMOVE_ADDRESS_COMMAND])
    name = args[0]
    contact_var = book.find_contact(name)
    return contact_var.remove_address()


@wrap_exception
def remove_birthday(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[
                constants.REMOVE_BIRTHDAY_COMMAND])
    name = args[0]
    contact_var = book.find_contact(name)
    return contact_var.remove_birthday()


@wrap_exception
def show_birthday(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SHOW_BIRTHDAY_COMMAND])
    days = args[0]
    try:
        if int(days) < 1 or int(days) > 365:
            raise ValueError
    except ValueError:
        raise exceptions.IncorrectArgsException("\[range] should be from 1 to 365")
    return get_birthdays_per_days_range(book.contacts, int(days))


@wrap_exception
def all_contacts(args, book):
    if len(args) != 0:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ALL_CONTACTS_COMMAND])

    return book.show_contacts(book.contacts.values())


@wrap_exception
def all_notes(args, book):
    if len(args) != 0:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ALL_NOTES_COMMAND])

    return book.show_notes(range(len(book.notes)), book.notes)


@wrap_exception
def remove_contact(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[
                constants.REMOVE_CONTACT_COMMAND])
    name = args[0]
    return book.remove_contact(name)


@wrap_exception
def add_phone(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_PHONE_COMMAND])
    name, phone = args
    contact_var = book.find_contact(name)
    return contact_var.add_phone(phone)


@wrap_exception
def set_address(args, book):
    if len(args) < 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_ADDRESS_COMMAND])
    name, address = args
    contact_var = book.find_contact(name)
    return contact_var.set_address(address)


@wrap_exception
def set_name(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_NAME_COMMAND])
    old_name, new_name = args
    contact_var = book.find_contact(old_name)

    try:
        book.find_contact(new_name)
        return f"Contact with {new_name} already exists. Please, edit the existing one."
    except exceptions.NoRecordException:
        pass

    return contact_var.set_name(new_name)


@wrap_exception
def set_birthday(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_BIRTHDAY_COMMAND])
    name, birthday = args
    contact_var = book.find_contact(name)
    return contact_var.set_birthday(birthday)


@wrap_exception
def set_email(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SET_EMAIL_COMMAND])
    name, email = args
    contact_var = book.find_contact(name)
    return contact_var.set_email(email)


@wrap_exception
def show_note(args, book):
    if len(args) < 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SHOW_NOTE_COMMAND])

    search_by, query = args[0].lower(), " ".join(args[1:])
    if search_by not in ["title", "content", "index"]:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.SHOW_NOTE_COMMAND])
    found_notes, found_indexes = book.find_note_by_search_value(query,
                                                                search_by)  # initializing found notes and indexes
    return book.show_notes(found_indexes, found_notes)


@wrap_exception
def add_tag_to_note(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.ADD_TAG_COMMAND])

    note_index = book.prepare_index(args[0])
    note_var = book.notes[note_index]
    return note_var.add_tag(args[1])


@wrap_exception
def remove_tag_from_note(args, book):
    if len(args) != 2:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_TAG_COMMAND])

    note_index = book.prepare_index(args[0])
    note_var = book.notes[note_index]
    return note_var.remove_tag(args[1])


@wrap_exception
def remove_all_tags_from_note(args, book):
    if len(args) != 1:
        raise exceptions.IncorrectArgsException(
            "Incorrect command format. Try " + constants.COMMAND_TO_COMMAND_FORMAT_MAP[constants.REMOVE_TAGS_COMMAND])

    note_index = book.prepare_index(args[0])
    note_var = book.notes[note_index]
    note_var.tags.clear()
    return f"Removed all tags from note at index {note_index + 1}."
