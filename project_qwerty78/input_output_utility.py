from .address_book import AddressBook
from . import contact
from . import note
import csv
from .easter_eggs import EasterEgg
from datetime import datetime

CONTACTS_FILE_NAME = "contacts_data.csv"
NOTES_FILE_NAME = "notes_data.csv"


def read_from_file():
    book = AddressBook()
    book.contacts = read_contacts_from_file()
    book.notes = read_notes_from_file()
    EasterEgg.ENABLED = True
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
                contact_var = contact.Contact(row["name"])

                if row["birthday"] != "None":
                    contact_var.set_birthday(row["birthday"])
                if row["email"] != "None":
                    contact_var.set_email(row["email"])
                if row["address"] != "None":
                    contact_var.set_address(row["address"])
                if row["phones"] != "None":
                    for phone in row["phones"].split(" "):
                        contact_var.add_phone(phone)
                contacts[row["name"].lower()] = contact_var
    finally:
        return contacts


def read_notes_from_file():
    notes = []

    try:
        with open(NOTES_FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                note_var = note.Note(row["content"])
                note_var.created_at = datetime.strptime(row["createdat"], '%Y-%m-%d %H:%M:%S')
                if row["title"] != "None":
                    note_var.set_title(row["title"])
                if row["tags"] != "None":
                    for tag in row["tags"].split(" "):
                        note_var.add_tag(tag)
                notes.append(note_var)
    finally:
        return notes


def write_contacts_to_file(contacts):
    with open(CONTACTS_FILE_NAME, "w") as f:
        field_names = ["name", "birthday", "email", "address", "phones"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for contact_var in contacts.values():
            writer.writerow({
                "name": str(contact_var.name),
                "birthday": str(contact_var.birthday),
                "email": str(contact_var.email),
                "address": str(contact_var.address),
                "phones": " ".join(str(phone) for phone in contact_var.phones) if len(
                    contact_var.phones) > 0 else "None"
            })


def write_notes_to_file(notes):
    with open(NOTES_FILE_NAME, "w") as f:
        field_names = ["title", "tags", "content", "createdat"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for note_var in notes:
            writer.writerow({
                "title": str(note_var.title),
                "tags": " ".join(str(tag) for tag in note_var.tags) if len(note_var.tags) > 0 else "None",
                "content": str(note_var.content),
                "createdat": note_var.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
