def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter a username."
        except Exception as e:
            return str(e)

    return inner


class ContactNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectArgsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
