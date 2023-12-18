from difflib import get_close_matches
from . import constants
def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        #TODO: add exceptions processing here
        except IndexError as e:
            return "Index out of range."
        except Exception as e:
            return e

    return inner

def process_command(command, args, book):
    
    
    return check_possible_commands(command)


def check_possible_commands(command):
    possible_commands = get_close_matches(command, constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys())
    for key in constants.COMMAND_TO_COMMAND_FORMAT_MAP.keys():
        if command in key or key in command:
            if key not in possible_commands:
                possible_commands.append(key)
    
    return (constants.INVALID_COMMAND 
            if len(possible_commands) == 0 
            else (f"{constants.INVALID_COMMAND}\nMaybe, you wanted to run one of these commands?\n\n" 
                  + "\n".join(constants.COMMAND_TO_COMMAND_FORMAT_MAP[x] for x in possible_commands)))