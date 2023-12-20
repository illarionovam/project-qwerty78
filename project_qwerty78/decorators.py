def confirm_remove(func):
    def inner(*args, **kwargs):
        user_input = input("Are you sure you want to remove the entry? There is no way back... (yes/no)")
        if user_input:
            user_input = user_input.strip().lower()
            if user_input in ["yes", "y"]:
                return func(*args, **kwargs)
        
        return "Remove operation was cancelled."            
    
    return inner


def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)

    return inner