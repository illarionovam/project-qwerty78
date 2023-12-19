import re
from datetime import datetime

from .field import Field


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("The number must be 10 characters long")


class Email(Field):
    def __init__(self, email):
        if self.is_valid_email(email):
            super().__init__(email)
        else:
            raise ValueError("The email is not valid")

    @staticmethod
    def is_valid_email(email):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None


class Address(Field):
    pass


class Birthday(Field):
    def __init__(self, date_string):
        date_object = self.is_valid_date(date_string)
        if date_object and date_object <= datetime.now():
            super().__init__(date_string)
        else:
            raise ValueError("The date of birth must be in the format DD.MM.YYYY and not later than today")

    @staticmethod
    def is_valid_date(date_string):
        try:
            return datetime.strptime(date_string, "%d.%m.%Y")
        except ValueError:
            return False


class Contact:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
