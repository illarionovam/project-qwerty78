from .address_book import AddressBook
import csv

CONTACTS_FILE_NAME = "contacts_data.csv"
NOTES_FILE_NAME = "notes_data.csv"


def read_from_file():
    book = AddressBook()
    book.data = read_contacts_from_file()
    book.notes = read_notes_from_file()
    return book


def write_to_file(book):
    write_contacts_to_file(book.contacts)
    write_notes_to_file(book.notes)


def read_contacts_from_file():
    contacts = {}

    try:
        with open(CONTACTS_FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                contact = contact.Contact(
                    contact.Name(row["name"]))
                
                if row["birthday"] != "None":
                    contact.add_birthday(row["birthday"])
                if row["email"] != "None":
                    contact.add_email(row["email"])
                if row["address"] != "None":
                    contact.add_address(row["address"])
                if row["phones"] != "None":
                    for phone in row["phones"].split(" "):
                        contact.add_phone(phone)
                contacts[row["name"]] = contact   
    finally:         
        return contacts  


def read_notes_from_file():
    notes = []

    try:
        with open(NOTES_FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                """note = note.Note(
                    note.Content(row["content"]))

                if row["title"] != "None":
                    note.add_title(row["title"])
                if row["tags"] != "None":
                    for tag in row["tags"].split(" "):
                        note.add_tag(tag)
                notes.append(note)
                """
    finally:            
        return notes  
    

def write_contacts_to_file(contacts):
    with open(CONTACTS_FILE_NAME, "w") as f:
        field_names = ["name", "birthday", "email", "address", "phones"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts.values():
            writer.writerow({
                "name": str(contact.name), 
                "birthday": str(contact.birthday),
                "email": str(contact.email),
                "address": str(contact.address),
                "phones": " ".join(str(phone) for phone in contact.phones) if len(contact.phones) > 0 else "None"
                })  
            

def write_notes_to_file(notes):
    with open(NOTES_FILE_NAME, "w") as f:
        field_names = ["title", "tags", "content"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        """for note in notes:
            writer.writerow({
                "title": str(note.title),
                "tags": " ".join(str(tag) for tag in note.tags) if len(note.tags) > 0 else "None",
                "content": str(note.content)
            })
            """