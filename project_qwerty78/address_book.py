from collections import UserDict
from . import exceptions
from .contact import get_contact_table
from .note import get_note_table
from .decorators import confirm_remove
from . import contact

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}
        self.notes = []

    def add_contact(self, contact):
        self.contacts[contact.name.value.lower()] = contact

    def find_contact(self, search_value):
        if contact.Birthday.is_valid(search_value):
            found = []
            for contact_var in self.contacts.values():
                if contact_var.birthday.value == search_value:
                    found.append(contact_var)
            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact {search_value}")
            return found
        if contact.Email.is_valid(search_value):
            found = []
            for contact_var in self.contacts.values():
                if contact_var.email.value == search_value:
                    found.append(contact_var)
            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact {search_value}")
            return found
        if contact.Phone.is_valid(search_value):
            found = []
            for contact_var in self.contacts.values():
                for phone in contact_var.phones:
                    if str(phone) == search_value:
                        found.append(contact_var)
                        break
            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact {search_value}")
            return found
        for key in self.contacts.keys():
            if name.lower() == key:
                return self.contacts[key]
        raise exceptions.NoRecordException(f"Contact {name}")
    
    @confirm_remove
    def remove_contact(self, name):
        self.find_contact(name) # raises exception if no contact exists
        if name.lower() in self.contacts.keys():
            self.contacts.pop(name.lower())
        return f"You have removed contact {name} from the address book."
    

    def all_contacts(self):
        if len(self.contacts) == 0:
            raise exceptions.EmptyContainerException("There are no contacts in the address book.")

        table = get_contact_table()

        for contact_var in self.contacts.values():
            table = contact_var.printable_view(table)

        return table
    

    def all_notes(self):
        if len(self.notes) == 0:
            raise exceptions.EmptyContainerException("There are no notes in the address book.")
        
        table = get_note_table()

        for i in range(len(self.notes)):
            note_var = self.notes[i]
            table = note_var.printable_view(table, i)

        return table
