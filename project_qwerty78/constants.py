INVALID_COMMAND = "Invalid command."
EXIT_COMMAND = "exit"
CLOSE_COMMAND = "close"
ADD_CONTACT_COMMAND = "add-contact"
ADD_PHONE_COMMAND = "add-phone"
ADD_BIRTHDAY_COMMAND = "add-birthday"
ADD_ADDRESS_COMMAND = "add-address"
ADD_EMAIL_COMMAND = "add-email"
SHOW_CONTACT_COMMAND = "show-contact"

EXIT_COMMANDS = [EXIT_COMMAND, CLOSE_COMMAND]

"""Because we are using rich module, we need to escape square brackets"""
COMMAND_TO_COMMAND_FORMAT_MAP = {
    CLOSE_COMMAND: CLOSE_COMMAND,
    EXIT_COMMAND: EXIT_COMMAND,
    ADD_CONTACT_COMMAND: ADD_CONTACT_COMMAND,
    ADD_PHONE_COMMAND: ADD_PHONE_COMMAND + " \[name] \[phone]",
    ADD_BIRTHDAY_COMMAND: ADD_BIRTHDAY_COMMAND + " \[name] \[birthday]",
    ADD_ADDRESS_COMMAND: ADD_ADDRESS_COMMAND + " \[name] \[address]",
    ADD_EMAIL_COMMAND: ADD_EMAIL_COMMAND + " \[name] \[email]",
    SHOW_CONTACT_COMMAND: SHOW_CONTACT_COMMAND + " \[name]"
}