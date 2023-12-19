from collections import UserDict
from . import exceptions


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}
        self.notes = []

    def add_record(self, contact):
        self.contacts[contact.name.value] = contact

    def find(self, name):
        for key in self.contacts.keys():
            if name.lower() == key.lower():
                return self.contacts[key]
        raise exceptions.NoContactException(name)