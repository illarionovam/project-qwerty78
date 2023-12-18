def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    #read from file

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
            #process command

            if command in ['close', 'exit'] and len(args) == 0:
                break
        except:
            print("Invalid command.")
    
    #write to file


if __name__ == "__main__":
    main()