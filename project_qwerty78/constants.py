INVALID_COMMAND = "Invalid command."
EXIT_COMMAND = "exit"
CLOSE_COMMAND = "close"
ADD_CONTACT_COMMAND = "add-contact"
ADD_PHONE_COMMAND = "add-phone"
SET_NAME_COMMAND = "set-name"
SET_BIRTHDAY_COMMAND = "set-birthday"
SET_ADDRESS_COMMAND = "set-address"
SET_EMAIL_COMMAND = "set-email"
SHOW_CONTACT_COMMAND = "show-contact"
REMOVE_CONTACT_COMMAND = "remove-contact"
REMOVE_EMAIL_COMMAND = "remove-email"
REMOVE_ADDRESS_COMMAND = "remove-address"
REMOVE_BIRTHDAY_COMMAND = "remove-birthday"
REMOVE_PHONES_COMMAND = "remove-phones"
REMOVE_PHONE_COMMAND = "remove-phone"
ALL_CONTACTS_COMMAND = "all-contacts"
ALL_NOTES_COMMAND = "all-notes"
SHOW_BIRTHDAY_COMMAND = "show-birthdays"
HELP_COMMAND = "help"
SHOW_NOTE_COMMAND = "show-note"
ADD_NOTE_COMMAND = "add-note"
ADD_TAG_COMMAND = "add-tag"
REMOVE_TAG_COMMAND = "remove-tag"

EXIT_COMMANDS = [EXIT_COMMAND, CLOSE_COMMAND]

"""Because we are using rich module, we need to escape square brackets"""
COMMAND_TO_COMMAND_FORMAT_MAP = {
    CLOSE_COMMAND: CLOSE_COMMAND,
    EXIT_COMMAND: EXIT_COMMAND,
    ADD_CONTACT_COMMAND: ADD_CONTACT_COMMAND,
    ADD_PHONE_COMMAND: ADD_PHONE_COMMAND + " \[name] \[phone]",
    SET_NAME_COMMAND: SET_NAME_COMMAND + " \[old_name] \[new_name]",
    SET_BIRTHDAY_COMMAND: SET_BIRTHDAY_COMMAND + " \[name] \[birthday]",
    SET_ADDRESS_COMMAND: SET_ADDRESS_COMMAND + " \[name] \[address]",
    SET_EMAIL_COMMAND: SET_EMAIL_COMMAND + " \[name] \[email]",
    SHOW_CONTACT_COMMAND: SHOW_CONTACT_COMMAND + " \[name]",
    REMOVE_CONTACT_COMMAND: REMOVE_CONTACT_COMMAND + " \[name]",
    REMOVE_EMAIL_COMMAND: REMOVE_EMAIL_COMMAND + " \[name]",
    REMOVE_ADDRESS_COMMAND: REMOVE_ADDRESS_COMMAND + " \[name]",
    REMOVE_BIRTHDAY_COMMAND: REMOVE_BIRTHDAY_COMMAND + " \[name]",
    REMOVE_PHONES_COMMAND: REMOVE_PHONES_COMMAND + " \[name]",
    REMOVE_PHONE_COMMAND: REMOVE_PHONE_COMMAND + " \[name] \[phone]",
    ALL_CONTACTS_COMMAND: ALL_CONTACTS_COMMAND,
    ALL_NOTES_COMMAND: ALL_NOTES_COMMAND,
    SHOW_BIRTHDAY_COMMAND: SHOW_BIRTHDAY_COMMAND + " \[range]",
    HELP_COMMAND: HELP_COMMAND,
    SHOW_NOTE_COMMAND: SHOW_NOTE_COMMAND + " \[title/content] \[query]",
    ADD_NOTE_COMMAND: ADD_NOTE_COMMAND,
    ADD_TAG_COMMAND: ADD_TAG_COMMAND + " \[note_title] \[tag]",
    REMOVE_TAG_COMMAND: REMOVE_TAG_COMMAND + " \[note_title] \[tag]",
}

COMMAND_TO_HELP_TEXT_MAP = {
    CLOSE_COMMAND: "Closes the bot.",
    EXIT_COMMAND: "Closes the bot.",
    ADD_CONTACT_COMMAND: "Adds contact to the address book.",
    ADD_PHONE_COMMAND: "Adds phone to the existing contact.",
    SET_NAME_COMMAND: "Sets new name for the existing contact.",
    SET_BIRTHDAY_COMMAND: "Sets birthday of the existing contact.",
    SET_ADDRESS_COMMAND: "Sets address of the existing contact.",
    SET_EMAIL_COMMAND: "Sets email of the existing contact.",
    SHOW_CONTACT_COMMAND: "Prints requested contacts.",
    REMOVE_CONTACT_COMMAND: "Removes contact from the address book.",
    REMOVE_EMAIL_COMMAND: "Removes email from the requested contact.",
    REMOVE_ADDRESS_COMMAND: "Removes address from the requested contact.",
    REMOVE_BIRTHDAY_COMMAND: "Removes birthday from the requested contact.",
    REMOVE_PHONES_COMMAND: "Removes all phones from the requested contact.",
    REMOVE_PHONE_COMMAND: "Removes requested phone from the requested contact.",
    ALL_CONTACTS_COMMAND: "Prints all contacts from the address book.",
    SHOW_BIRTHDAY_COMMAND: "Shows coming contacts' birthdays in the next N days.",
    HELP_COMMAND: "Help menu.",
    SHOW_NOTE_COMMAND: "Prints requested notes by either title or content.",
    ADD_NOTE_COMMAND: "Adds note to the address book.",
    ADD_TAG_COMMAND: "Adds a tag to a note by title.",
    REMOVE_TAG_COMMAND: "Removes a tag from a note by title."
}