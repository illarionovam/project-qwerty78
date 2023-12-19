import re
from datetime import datetime

from .constants import CONTACT_NOT_FOUND
from .exceptions import IncorrectArgsException, wrap_exception, ContactNotFoundException
from .field import Field


class Name(Field):
    def __init__(self, name):
        if not name:
            raise IncorrectArgsException("Name cannot be empty")
        super().__init__(name)


class Phone(Field):
    def __init__(self, value):
        if self.is_valid_phone(value):
            super().__init__(value)
        else:
            raise IncorrectArgsException("The number must be 10 characters long")

    @staticmethod
    def is_valid_phone(phone):
        return re.fullmatch(r"\d{10}", phone) is not None


class Email(Field):
    def __init__(self, email):
        if self.is_valid_email(email):
            super().__init__(email)
        else:
            raise IncorrectArgsException("The email is not valid")

    @staticmethod
    def is_valid_email(email):
        email_regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[" \
                      "\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[" \
                      "\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[" \
                      "a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][" \
                      "0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[" \
                      "\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[" \
                      "\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\]) "
        return re.match(email_regex, email) is not None


class Address(Field):
    pass


class Birthday(Field):
    def __init__(self, date_string):
        date_object = self.is_valid_date(date_string)
        if date_object:
            super().__init__(date_string)
        else:
            raise IncorrectArgsException("The date of birth must be in the format DD.MM.YYYY and not later than today")

    @staticmethod
    def is_valid_date(date_string):
        try:
            date_object = datetime.strptime(date_string, "%d.%m.%Y")
            return date_object and date_object <= datetime.now()
        except ValueError:
            return False


class Contact:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    @staticmethod
    @wrap_exception
    def add_contact(args, address_book):
        name = args[0]
        phone = args[1] if args[1] != '' else None
        birthday = args[2] if args[2] != '' else None
        email = args[3] if args[3] != '' else None
        address = args[4] if args[4] != '' else None

        contact = Contact(name, phone, birthday, email, address)
        address_book.add_record(contact)
        return "contact added"

    @staticmethod
    @wrap_exception
    def add_phone(args, address_book):
        if len(args) != 2:
            raise IncorrectArgsException("Enter name and phone")
        name, phone = args
        contact = address_book.find(name)
        if contact:
            if Phone.is_valid_phone(phone):
                if phone not in contact.phones:
                    contact.phones.append(phone)
                    return "Phone number added"
                else:
                    return "Phone number already exists"
            else:
                raise IncorrectArgsException("The number must be 10 characters long")
        else:
            raise ContactNotFoundException(CONTACT_NOT_FOUND)

    @staticmethod
    @wrap_exception
    def add_address(args, address_book):
        if len(args) < 2:
            raise IncorrectArgsException("Enter name and address")
        name, address = args
        contact = address_book.find(name)
        if contact:
            contact.address(address)
            return "Address added"
        else:
            raise ContactNotFoundException(CONTACT_NOT_FOUND)

    @staticmethod
    @wrap_exception
    def add_birthday(args, address_book):
        if len(args) != 2:
            raise IncorrectArgsException("Enter name and birthday date")
        name, birthday = args
        contact = address_book.find(name)
        if contact:
            contact.birthday(birthday)
            return "Birthday date added"
        else:
            raise ContactNotFoundException(CONTACT_NOT_FOUND)

    @staticmethod
    @wrap_exception
    def add_email(args, address_book):
        if len(args) != 2:
            raise IncorrectArgsException("Enter name and email")
        name, email = args
        contact = address_book.find(name)
        if contact:
            contact.email(email)
            return "Email added"
        else:
            raise ContactNotFoundException(CONTACT_NOT_FOUND)
