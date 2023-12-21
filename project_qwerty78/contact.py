import re
from datetime import datetime
from rich.table import Table
from rich.style import Style
from .exceptions import IncorrectArgsException
from .field import Field
from .easter_eggs import EasterEgg
from .decorators import confirm_remove


def get_contact_table():
    table = Table(show_lines=True)

    header_style = Style(bgcolor="rgb(0,87,184)")
    table_style = Style(bgcolor="rgb(255,215,0)")
    for column in ["Name", "Phones", "Email", "Birthday", "Address"]:
        table.add_column(column, header_style=header_style, style=table_style)

    return table


class Name(Field):
    def __init__(self, name):
        """Checks is the name is not empty. 
        Casts name to .title()
        """
        if Name.is_valid(name):
            if EasterEgg.ENABLED:
                EasterEgg.is_interesting_name(name)
            super().__init__(name.title())
        else:
            if name == "":
                raise IncorrectArgsException("A girl has no name? No chance!")
            raise IncorrectArgsException("Their dad must be Elon Musk... So sorry, but only latin letters are allowed")

    @staticmethod
    def is_valid(name):
        return re.fullmatch(r"[a-zA-Z]+", name) is not None


class Phone(Field):
    def __init__(self, phone):
        if Phone.is_valid(phone):
            if EasterEgg.ENABLED:
                EasterEgg.is_interesting_phone(phone)
            super().__init__(phone)
        else:
            raise IncorrectArgsException("The phone must be 10 characters long")

    @staticmethod
    def is_valid(phone):
        return re.fullmatch(r"\d{10}", phone) is not None


class Email(Field):
    def __init__(self, email):
        if Email.is_valid(email):
            super().__init__(email.lower())
        else:
            raise IncorrectArgsException("The email is not valid")

    @staticmethod
    def is_valid(email):
        return re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', email) is not None


class Address(Field):
    pass


class Birthday(Field):
    def __init__(self, date_string):
        if Birthday.is_valid(date_string):
            date_string = Birthday.cast_to_standard_format(date_string)
            if EasterEgg.ENABLED:
                EasterEgg.is_interesting_birthday(date_string)
            super().__init__(date_string)
        else:
            raise IncorrectArgsException("The birthday date must be in the format DD.MM.YYYY and not later than today")
        
    @staticmethod
    def cast_to_standard_format(date_string):
        date_object = datetime.strptime(date_string, "%d.%m.%Y")
        return date_object.strftime("%d.%m.%Y")

    @staticmethod
    def is_valid(date_string):
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

    def printable_view(self, table):
        table.add_row(
            str(self.name), 
            "\n".join(str(phone) for phone in self.phones), 
            str(self.email) if self.email else "", 
            str(self.birthday) if self.birthday else "", 
            re.sub("\[", "\\[", str(self.address)) if self.address else "")
        
        return table
    
    def add_phone(self, phone):
        result = list(filter(lambda phone_obj: phone_obj.value == phone, self.phones))
        if len(result) > 0:
            return "Phone already exists."
        else:
            self.phones.append(Phone(phone))
            return "Added phone."  

    def set_name(self, name):
        self.name = Name(name)
        return "Updated name."          
        
    def set_address(self, address):
        overriden = (self.address != None)
        self.address = Address(address)
        return "Updated address." if overriden else "Added address."
    
    def set_birthday(self, birthday):
        overriden = (self.birthday != None)
        self.birthday = Birthday(birthday)
        return "Updated birthday." if overriden else "Added birthday."
        
    def set_email(self, email):
        overriden = (self.email != None)
        self.email = Email(email)
        return "Updated email." if overriden else "Added email."
        
    @confirm_remove
    def remove_email(self):
        self.email = None
        return "Removed email."
    
    @confirm_remove
    def remove_address(self):
        self.address = None
        return "Removed address."
    
    @confirm_remove
    def remove_phones(self):
        self.phones = []
        return "Removed all phones."
    
    @confirm_remove
    def remove_phone(self, phone):
        self.phones = list(filter(lambda phone_obj: phone_obj.value != phone, self.phones))
        return "Removed phone."
    
    @confirm_remove
    def remove_birthday(self):
        self.birthday = None
        return "Removed birthday."