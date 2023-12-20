INVALID_COMMAND = "Invalid command."
EXIT_COMMAND = "exit"
CLOSE_COMMAND = "close"
ADD_CONTACT_COMMAND = "add-contact"
ADD_PHONE_COMMAND = "add-phone"
UPDATE_BIRTHDAY_COMMAND = "update-birthday"
UPDATE_ADDRESS_COMMAND = "update-address"
UPDATE_EMAIL_COMMAND = "update-email"
SHOW_CONTACT_COMMAND = "show-contact"
REMOVE_CONTACT_COMMAND = "remove-contact"
ALL_CONTACTS_COMMAND = "all-contacts"
SHOW_BIRTHDAY_COMMAND = "show-birthdays"
HELP_COMMAND = "help"

EXIT_COMMANDS = [EXIT_COMMAND, CLOSE_COMMAND]

"""Because we are using rich module, we need to escape square brackets"""
COMMAND_TO_COMMAND_FORMAT_MAP = {
    CLOSE_COMMAND: CLOSE_COMMAND,
    EXIT_COMMAND: EXIT_COMMAND,
    ADD_CONTACT_COMMAND: ADD_CONTACT_COMMAND,
    ADD_PHONE_COMMAND: ADD_PHONE_COMMAND + " \[name] \[phone]",
    UPDATE_BIRTHDAY_COMMAND: UPDATE_BIRTHDAY_COMMAND + " \[name] \[birthday]",
    UPDATE_ADDRESS_COMMAND: UPDATE_ADDRESS_COMMAND + " \[name] \[address]",
    UPDATE_EMAIL_COMMAND: UPDATE_EMAIL_COMMAND + " \[name] \[email]",
    SHOW_CONTACT_COMMAND: SHOW_CONTACT_COMMAND + " \[name]",
    REMOVE_CONTACT_COMMAND: REMOVE_CONTACT_COMMAND + " \[name]",
    ALL_CONTACTS_COMMAND: ALL_CONTACTS_COMMAND,
    SHOW_BIRTHDAY_COMMAND: SHOW_BIRTHDAY_COMMAND + " \[range]",
    HELP_COMMAND: HELP_COMMAND
}

COMMAND_TO_HELP_TEXT_MAP = {
    CLOSE_COMMAND: "Closes the bot.",
    EXIT_COMMAND: "Closes the bot.",
    ADD_CONTACT_COMMAND: "Adds contact to the address book.",
    ADD_PHONE_COMMAND: "Adds phone to the existing contact.",
    UPDATE_BIRTHDAY_COMMAND: "Updates birthday of the existing contact.",
    UPDATE_ADDRESS_COMMAND: "Updates address of the existing contact.",
    UPDATE_EMAIL_COMMAND: "Updates email of the existing contact.",
    SHOW_CONTACT_COMMAND: "Prints requested contact.",
    REMOVE_CONTACT_COMMAND: "Removes contact from the address book.",
    ALL_CONTACTS_COMMAND: "Prints all contacts from the address book.",
    SHOW_BIRTHDAY_COMMAND: "Shows coming contacts' birthdays in the next N days.",
    HELP_COMMAND: "Help menu."
}