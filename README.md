# Personal assistant

Personal assistant bot is a console application that helps you to maintain your contacts and notes. 

You can add phones, birthday, email and address to the contacts, edit contacts and remove them. 

You can add title and tags to the notes, edit notes and remove them. You can sort your notes by the date added and tags.

It saves your data locally on your machine.

## Instalation process

### Via github

1. Download ZIP.
2. Extract.
3. Run `bot_outside_ns.py`.

### Via pip

1. Run `python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps project_qwerty78==0.0.0`
2. Start the bot with `run_bot` in the console.

## Commands

All commands are *case-insensitive*.

The bot will try to guess the command if the user makes a typo.

For the remove commands, the bot will ask you to confirm the command.

On particular input bot can react with hidden easter eggs. Try to find them if you want 😉

### Utility commands

- `close` or `exit`
    - Closes the bot.

- `help`
    - Shows manual for the bot execution.

### Commands to work with contacts

- `add-contact`
    - Adds contact to the address book. In the appeared prompt, the user should provide name (required), phone, birthday, email, address.

- `show-contact [search_value]`
    - Prints requested contacts. `[search_value]` can be name, birthday, email, phone.

- `remove-contact [name]`
    - Removes contact `[name]` from the address book.

- `set-name [old_name] [new_name]`
    - Sets `[new_name]` for the existing contact `[old_name]`.

- `add-phone [name] [phone]`
    - Adds `[phone]` to the existing contact `[name]`.

- `remove-phone [name] [phone]`
    - Removes `[phone]` from the existing contact `[name]`.

- `remove-phones [name]`
    - Removes all phones from the existing contact `[name]`.

- `set-birthday [name] [birthday]`
    - Sets `[birthday]` of the existing contact `[name]`.

- `remove-birthday [name]`
    - Removes birthday from the existing contact `[name]`.

- `set-email [name] [email]`
    - Sets `[email]` of the existing contact `[name]`. Emails are case-insensitive.

- `remove-email [name]`
    - Removes email from the existing contact `[name]`.

- `set-address [name] [address]`
    - Sets `[address]` of the existing contact `[name]`.

- `remove-address [name]`
    - Removes address from the existing contact `[name]`.

- `show-birthdays [range]`
    - Shows coming contacts' birthdays in the next `[range]` days.

- `all-contacts`
    - Prints all contacts from the address book.

### Commands to work with notes

- `add-note`
    - Adds note to the address book. In the appeared prompt, the user should provide title, content (required).

- `show-note [index/title/content] [query]`
    - Prints requested notes by either index, title or content.

- `remove-note [index]`
    - Removes note `[index]` from the address book.

- `add-tag [index] [tag]`
    - Adds `[tag]` to the existing note `[index]`.

- `remove-tag [index] [tag]`
    - Removes `[tag]` from the existing note `[index]`.

- `remove-tags [index]`
    - Removes all tags from the existing note `[index]`.

- `all-notes`
    - Prints all notes from the address book.

## Data validation

- Name
    - Should contain only latin letters.
- Phone
    - Should be 10 digits.
- Email
    - Should be in format `[suffix]`@`[domain]`.`[top_domain]`.
    - `[suffix]` - can contain latin letters (lower or upper), digits, `_` or `.`. Should start with a latin letter. Should contain at least 2 characters.
    - `[domain]` - can contain letin letters (lower or upper). Should contain at least 1 character.
    - `[top_domain]` - can contain letin letters (lower or upper). Should contain at least 2 character.
- Birthday
    - Should be a valid date (that is less or equal to today's date) in format `DD.MM.YYYY`.
- Title
    - Should contain only latin letters, digits and spaces, no longer than 15 characters.
- Tag
    - Should contain only latin letters and digits, no longer than 10 characters. 

## Data constancy between bot's executions

- Contacts are saved to `contacts_data.csv`.

- Notes are saved to `notes_data.csv`.