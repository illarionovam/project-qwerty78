import re
from datetime import datetime
from rich.table import Table
from .exceptions import IncorrectArgsException
from .field import Field


def get_contact_table():
    table = Table(show_lines=True)

    table.add_column("Name", style="black on green")
    table.add_column("Phones", style="magenta on cyan")
    table.add_column("Email", style="magenta")
    table.add_column("Birthday", style="magenta")
    table.add_column("Address", style="magenta")

    return table


class Name(Field):
    def __init__(self, name):
        """Checks is the name is not empty. 
        Casts name to .title()
        """
        if Name.is_valid(name):
            super().__init__(name.title())
        else:
            raise IncorrectArgsException("Name cannot be empty and should contain only latin letters")
        

    @staticmethod
    def is_valid(name):
        return re.fullmatch(r"[a-zA-Z]+", name) is not None


class Phone(Field):
    def __init__(self, value):
        if Phone.is_valid(value):
            super().__init__(value)
        else:
            raise IncorrectArgsException("The number must be 10 characters long")

    @staticmethod
    def is_valid(phone):
        return re.fullmatch(r"\d{10}", phone) is not None


class Email(Field):
    def __init__(self, email):
        if Email.is_valid(email):
            super().__init__(email)
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
            super().__init__(date_string)
        else:
            raise IncorrectArgsException("The date of birth must be in the format DD.MM.YYYY and not later than today")

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
            return "Phone number already exists"
        else:
            self.phones.append(Phone(phone))
            return "Phone number added"  

    def set_name(self, name):
        self.name = Name(name)
        return "Name updated"          
        
    def set_address(self, address):
        overriden = (self.address != None)
        self.address = Address(address)
        return "Address updated" if overriden else "Address added"
    
    def set_birthday(self, birthday):
        overriden = (self.birthday != None)
        self.birthday = Birthday(birthday)
        return "Birthday updated" if overriden else "Birthday added"
        
    def set_email(self, email):
        overriden = (self.email != None)
        self.email = Email(email)
        return "Email updated" if overriden else "Email added"
        