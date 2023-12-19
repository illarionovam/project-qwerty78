from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name.value] = contact
