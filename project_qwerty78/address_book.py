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

    def find_contact_by_search_value(self, search_value):
        found = []

        if contact.Birthday.is_valid(search_value):   
            for contact_var in self.contacts.values():
                if contact_var.birthday and contact_var.birthday.value == search_value:
                    found.append(contact_var)

            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with BD {search_value}")
            
            return found
        elif contact.Email.is_valid(search_value):
            for contact_var in self.contacts.values():
                if contact_var.email and contact_var.email.value == search_value.lower():
                    found.append(contact_var)

            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with email {search_value}")
            
            return found
        elif contact.Phone.is_valid(search_value):
            for contact_var in self.contacts.values():
                for phone in contact_var.phones:
                    if phone.value == search_value:
                        found.append(contact_var)
                        break
            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with phone {search_value}")  

            return found   
        else:
            return [self.find_contact(search_value)]

    def find_contact(self, name):
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
    

    def show_contacts(self, explicit_contacts):
        if len(explicit_contacts) == 0:
            raise exceptions.EmptyContainerException("There are no contacts in the address book.")

        table = get_contact_table()

        for contact_var in explicit_contacts:
            table = contact_var.printable_view(table)

        return table
    

    def show_notes(self, indeces, explicit_notes):
        if len(explicit_notes) == 0:
            raise exceptions.EmptyContainerException("There are no notes in the address book.")
        
        table = get_note_table()

        for i in range(len(indeces)):
            note_var = self.notes[i]
            table = note_var.printable_view(table, indeces[i])

        return table
