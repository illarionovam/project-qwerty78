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
        super().__init__()

    def prepare_index(self, index):
        try:
            index = int(index)
            if index < 1 or index > len(self.notes):
                raise exceptions.IncorrectArgsException(
                    f"Invalid index {index}. Should be an integer from 1 to {len(self.notes)}")
            return index - 1
        except ValueError:
            raise exceptions.IncorrectArgsException(
                f"Invalid index {index}. Should be an integer from 1 to {len(self.notes)}")

    def add_note(self, note):
        self.notes.append(note)

    def add_contact(self, contact):
        self.contacts[contact.name.value.lower()] = contact

    def find_contact_by_search_value(self, search_value):
        found = []

        if contact.Birthday.is_valid(search_value):
            for contact_var in self.contacts.values():
                if contact_var.birthday and contact_var.birthday.value == contact.Birthday.cast_to_standard_format(
                        search_value):
                    found.append(contact_var)

            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with the birthday {search_value}")

            return found
        elif contact.Email.is_valid(search_value):
            for contact_var in self.contacts.values():
                if contact_var.email and contact_var.email.value == search_value.lower():
                    found.append(contact_var)

            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with the email {search_value}")

            return found
        elif contact.Phone.is_valid(search_value):
            for contact_var in self.contacts.values():
                for phone in contact_var.phones:
                    if phone.value == search_value:
                        found.append(contact_var)
                        break
            if len(found) == 0:
                raise exceptions.NoRecordException(f"Contact with the phone {search_value}")

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
        self.find_contact(name)  # raises exception if no contact exists
        if name.lower() in self.contacts.keys():
            self.contacts.pop(name.lower())
        return f"Removed contact {name} from the address book."

    def show_contacts(self, explicit_contacts):
        if len(explicit_contacts) == 0:
            raise exceptions.EmptyContainerException("There are no contacts in the address book.")

        table = get_contact_table()

        for contact_var in explicit_contacts:
            table = contact_var.printable_view(table)

        return table

    def show_notes(self, indexes, explicit_notes):
        if len(explicit_notes) == 0:
            raise exceptions.EmptyContainerException("There are no notes in the address book.")

        table = get_note_table()

        for i in range(len(indexes)):
            note_var = self.notes[indexes[i]]
            table = note_var.printable_view(table, indexes[i])

        return table

    def find_note_by_search_value(self, query, search_by):
        if search_by == "index":
            index = self.prepare_index(query)
            return [self.find_note(index)], [index]

        matched_notes = []
        matched_indexes = []
        for index, note in enumerate(self.notes):
            if (search_by == "title" and note.matches_title(query)) or \
                    (search_by == "content" and note.matches_content(query)):
                matched_notes.append(note)
                matched_indexes.append(index)

        if len(matched_notes) == 0:
            raise exceptions.NoRecordException(f"Note with the {search_by} {query}")

        return matched_notes, matched_indexes

    def find_note(self, index):
        return self.notes[index]

    @confirm_remove
    def remove_note(self, index):
        del self.notes[index]
        return f"Removed the note at index {index + 1}."
    
    def show_notes_by_tag(self, tag):
        normalized_tag = tag.lower()
        found_notes_with_indexes = [(index, note) for index, note in enumerate(self.notes, start=1) 
        if normalized_tag in (t.lower() for t in note.tags)]

        if not found_notes_with_indexes:
            raise exceptions.EmptyContainerException(f"No notes with tag '{tag}' found.")

        table = get_note_table()

        for original_index, note in found_notes_with_indexes:
            tags = ', '.join(sorted(note.tags))
            table.add_row(str(original_index), note.title.value if note.title else "", tags, note.content.value)

        return table


    def sort_notes_asc(self):
        sorted_notes_with_indexes = sorted(
            enumerate(self.notes, start=1), 
            key=lambda x: sorted(x[1].tags) if x[1].tags else []
        )
        return self.format_notes_for_display(sorted_notes_with_indexes)


    def sort_notes_desc(self):
        sorted_notes_with_indexes = sorted(
            enumerate(self.notes, start=1), 
            key=lambda x: sorted(x[1].tags, reverse=True) if x[1].tags else [],
            reverse=True
        )
        return self.format_notes_for_display(sorted_notes_with_indexes)

   
    def format_notes_for_display(self, notes_with_indexes):
        if not notes_with_indexes:
            raise exceptions.EmptyContainerException("There are no notes in the address book.")

        table = get_note_table()
        for original_index, note in notes_with_indexes:
            tags = ', '.join(sorted(note.tags) if note.tags else '')
            created_at = note.created_at.strftime('%Y-%m-%d %H:%M:%S') 
            table.add_row(
                str(original_index), 
                note.title.value if note.title else "", 
                tags, 
                note.content.value,
                created_at 
            )
        return table
    
    
    def sort_notes_by_date_asc(self):
        sorted_notes_with_indexes = sorted(
            enumerate(self.notes, start=1), 
            key=lambda x: x[1].created_at
        )
        return self.format_notes_for_display(sorted_notes_with_indexes)

    def sort_notes_by_date_desc(self):
        sorted_notes_with_indexes = sorted(
            enumerate(self.notes, start=1), 
            key=lambda x: x[1].created_at,
            reverse=True
        )
        return self.format_notes_for_display(sorted_notes_with_indexes)