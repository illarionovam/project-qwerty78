from .bot_utility import process_command
from .constants import INVALID_COMMAND, EXIT_COMMANDS
from rich.console import Console
from .input_output_utility import read_from_file, write_to_file


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = read_from_file()
    console = Console()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            try:
                command, *args = parse_input(user_input)
                console.print(process_command(command, args, book))

                if command in EXIT_COMMANDS and len(args) == 0:
                    break
            except:
                print(INVALID_COMMAND)

    write_to_file(book)


if __name__ == "__main__":
    main()
