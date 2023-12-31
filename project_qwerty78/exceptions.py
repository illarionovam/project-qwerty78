class NoRecordException(Exception):
    def __init__(self, record):
        self.message = f"{record} was not found."
        super().__init__(self.message)


class IncorrectArgsException(Exception):
    def __init__(self, message):
        if not message.endswith("!"):
            message = message + "."
        self.message = message
        super().__init__(self.message)


class EmptyContainerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
