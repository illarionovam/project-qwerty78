from collections import UserDict

from .constants import CONTACT_NOT_FOUND


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find(self, name):
        return self.data.get(name, CONTACT_NOT_FOUND)
