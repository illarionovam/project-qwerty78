
from collections import UserDict
from . import exceptions
from .contact import get_contact_table
from .decorators import confirm_remove

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

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
    
    @confirm_remove
    def remove_contact(self, name):
        self.find_contact(name) # raises exception if no contact exists
        if name.lower() in self.contacts.keys():
            self.contacts.pop(name.lower())
        return f"You have removed contact {name} from the address book."
    

    def all_contacts(self):
        if len(self.contacts) == 0:
            raise exceptions.EmptyContactsException("There are no contacts in the address book.")

        table = get_contact_table()

        for contact_var in self.contacts.values():
            table = contact_var.printable_view(table)

        return table

    def add_note(self, title, content):
        self.notes.append(Note(title, content))
    def delete_note_by_index(self, index):
        del self.notes[index]
    def edit_note_by_index(self, index, title, content):
        self.notes[index].title = title
        self.notes[index].content = content

