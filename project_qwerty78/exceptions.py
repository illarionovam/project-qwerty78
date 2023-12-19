def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)

    return inner


class NoContactException(Exception):
    def __init__(self, name):
        self.message = f"Contact {name} not found."
        super().__init__(self.message)


class IncorrectArgsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EmptyContactsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)