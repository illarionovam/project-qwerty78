from collections import UserDict
from . import exceptions


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}
        self.notes = []

    def add_contact(self, contact):
        self.contacts[contact.name.value.lower()] = contact

    def find_contact(self, name):
        for key in self.contacts.keys():
            if name.lower() == key:
                return self.contacts[key]
        raise exceptions.NoContactException(name)
    
    def remove_contact(self, name):
        if name.lower() in self.contacts.keys():
            self.contacts.pop(name.lower())
        return f"You have removed contact {name} from the address book."