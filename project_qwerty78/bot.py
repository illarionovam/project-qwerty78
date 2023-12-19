from .bot_utility import process_command
from .constants import INVALID_COMMAND, EXIT_COMMANDS
from .address_book import AddressBook
from rich.console import Console


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    # read from file
    address_book = AddressBook()
    console = Console()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
            console.print(process_command(command, args, address_book))

            if command in EXIT_COMMANDS and len(args) == 0:
                break
        except Exception as e:
            print(e)
            print(INVALID_COMMAND)

    # write to file


if __name__ == "__main__":
    main()
