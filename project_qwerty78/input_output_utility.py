from .address_book import AddressBook
from . import contact
from . import note
import csv

CONTACTS_FILE_NAME = "contacts_data.csv"
NOTES_FILE_NAME = "notes_data.csv"


def read_from_file():
    book = AddressBook()
    book.data = read_contacts_from_file()
    book.notes = read_notes_from_file()
    return book


def read_contacts_from_file():
    contacts = {}

    try:
        with open(CONTACTS_FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                """contact = contact.Contact(
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
                """
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