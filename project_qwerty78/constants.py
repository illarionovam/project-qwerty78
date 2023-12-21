RED_COLOR = "rgb(221,0,81)"
ERROR_STYLE = f"[on {RED_COLOR}]"

INVALID_COMMAND = "Invalid command."
# Utility commands
EXIT_COMMAND = "exit"
CLOSE_COMMAND = "close"
HELP_COMMAND = "help"
# Commands to work with contacts
ADD_CONTACT_COMMAND = "add-contact"
SHOW_CONTACT_COMMAND = "show-contact"
REMOVE_CONTACT_COMMAND = "remove-contact"
SET_NAME_COMMAND = "set-name"
ADD_PHONE_COMMAND = "add-phone"
REMOVE_PHONE_COMMAND = "remove-phone"
REMOVE_PHONES_COMMAND = "remove-phones"
SET_BIRTHDAY_COMMAND = "set-birthday"
REMOVE_BIRTHDAY_COMMAND = "remove-birthday"
SET_EMAIL_COMMAND = "set-email"
REMOVE_EMAIL_COMMAND = "remove-email"
SET_ADDRESS_COMMAND = "set-address"
REMOVE_ADDRESS_COMMAND = "remove-address"
SHOW_BIRTHDAY_COMMAND = "show-birthdays"
ALL_CONTACTS_COMMAND = "all-contacts"
# Commands to work with notes
ADD_NOTE_COMMAND = "add-note"
SHOW_NOTE_COMMAND = "show-note"
REMOVE_NOTE_COMMAND = "remove-note"
ADD_TAG_COMMAND = "add-tag"
REMOVE_TAG_COMMAND = "remove-tag"
REMOVE_TAGS_COMMAND = "remove-tags"
SET_TITLE_COMMAND = "set-title"
SET_CONTENT_COMMAND = "set-content"
ALL_NOTES_COMMAND = "all-notes"

EXIT_COMMANDS = [EXIT_COMMAND, CLOSE_COMMAND]

"""Because we are using rich module, we need to escape square brackets"""
COMMAND_TO_COMMAND_FORMAT_MAP = {
    CLOSE_COMMAND: CLOSE_COMMAND,
    EXIT_COMMAND: EXIT_COMMAND,
    HELP_COMMAND: HELP_COMMAND,
    ADD_CONTACT_COMMAND: ADD_CONTACT_COMMAND,
    SHOW_CONTACT_COMMAND: SHOW_CONTACT_COMMAND + " \[search_value]",
    REMOVE_CONTACT_COMMAND: REMOVE_CONTACT_COMMAND + " \[name]",
    SET_NAME_COMMAND: SET_NAME_COMMAND + " \[old_name] \[new_name]",
    ADD_PHONE_COMMAND: ADD_PHONE_COMMAND + " \[name] \[phone]",
    REMOVE_PHONE_COMMAND: REMOVE_PHONE_COMMAND + " \[name] \[phone]",
    REMOVE_PHONES_COMMAND: REMOVE_PHONES_COMMAND + " \[name]",   
    SET_BIRTHDAY_COMMAND: SET_BIRTHDAY_COMMAND + " \[name] \[birthday]",
    REMOVE_BIRTHDAY_COMMAND: REMOVE_BIRTHDAY_COMMAND + " \[name]",
    SET_EMAIL_COMMAND: SET_EMAIL_COMMAND + " \[name] \[email]",
    REMOVE_EMAIL_COMMAND: REMOVE_EMAIL_COMMAND + " \[name]",
    SET_ADDRESS_COMMAND: SET_ADDRESS_COMMAND + " \[name] \[address]",
    REMOVE_ADDRESS_COMMAND: REMOVE_ADDRESS_COMMAND + " \[name]",  
    SHOW_BIRTHDAY_COMMAND: SHOW_BIRTHDAY_COMMAND + " \[range]",  
    ALL_CONTACTS_COMMAND: ALL_CONTACTS_COMMAND,    
    ADD_NOTE_COMMAND: ADD_NOTE_COMMAND,
    SHOW_NOTE_COMMAND: SHOW_NOTE_COMMAND + " \[index/title/content] \[query]",
    REMOVE_NOTE_COMMAND: REMOVE_NOTE_COMMAND + " \[index]",
    ADD_TAG_COMMAND: ADD_TAG_COMMAND + " \[index] \[tag]",
    REMOVE_TAG_COMMAND: REMOVE_TAG_COMMAND + " \[index] \[tag]",
    REMOVE_TAGS_COMMAND: REMOVE_TAGS_COMMAND + " \[index]",
    SET_TITLE_COMMAND: SET_TITLE_COMMAND + " \[index] \[title]",
    SET_CONTENT_COMMAND: SET_CONTENT_COMMAND + " \[index] \[content]",
    ALL_NOTES_COMMAND: ALL_NOTES_COMMAND    
}

COMMAND_TO_HELP_TEXT_MAP = {
    CLOSE_COMMAND: "Closes the bot.",
    EXIT_COMMAND: "Closes the bot.",
    HELP_COMMAND: "Shows manual for the bot execution.",
    ADD_CONTACT_COMMAND: "Adds contact to the address book.",
    SHOW_CONTACT_COMMAND: "Prints requested contacts.",
    REMOVE_CONTACT_COMMAND: "Removes contact \[name] from the address book.",
    SET_NAME_COMMAND: "Sets \[new_name] for the existing contact \[old_name].",
    ADD_PHONE_COMMAND: "Adds \[phone] to the existing contact \[name].",
    REMOVE_PHONE_COMMAND: "Removes \[phone] from the existing contact \[name].",
    REMOVE_PHONES_COMMAND: "Removes all phones from the existing contact \[name].",
    SET_BIRTHDAY_COMMAND: "Sets \[birthday] of the existing contact \[name].",
    REMOVE_BIRTHDAY_COMMAND: "Removes birthday from the existing contact \[name].",
    SET_EMAIL_COMMAND: "Sets \[email] of the existing contact \[name].",
    REMOVE_EMAIL_COMMAND: "Removes email from the existing contact \[name].",
    SET_ADDRESS_COMMAND: "Sets \[address] of the existing contact \[name].",
    REMOVE_ADDRESS_COMMAND: "Removes address from the existing contact \[name].",
    SHOW_BIRTHDAY_COMMAND: "Shows coming contacts' birthdays in the next \[range] days.",    
    ALL_CONTACTS_COMMAND: "Prints all contacts from the address book.",
    ADD_NOTE_COMMAND: "Adds note to the address book.",
    SHOW_NOTE_COMMAND: "Prints requested notes by either index, title or content.",
    REMOVE_NOTE_COMMAND: "Removes note \[index] from the address book.",
    ADD_TAG_COMMAND: "Adds \[tag] to the existing note \[index].",
    REMOVE_TAG_COMMAND: "Removes \[tag] from the existing note \[index].",
    REMOVE_TAGS_COMMAND: "Removes all tags from the existing note \[index].",
    SET_TITLE_COMMAND: "Sets \[title] for the axisting note \[index].",
    SET_CONTENT_COMMAND: "Sets \[content] for the axisting note \[index].",
    ALL_NOTES_COMMAND: "Prints all notes from the address book."
}
