from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Content(Field):
    pass


class Tag(Field):
    pass


class Phone(Field):
    pass
        

class Email(Field):
    pass


class Address(Field):
    pass


class Birthday(Field):
    pass


class Note:
    pass


class Record:
    pass


class AddressBook(UserDict):
    pass