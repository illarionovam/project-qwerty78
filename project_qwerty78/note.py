from .field import Field
import re
from .exceptions import IncorrectArgsException


class Title(Field):
    def __init__(self, title):
        if Title.is_valid(title):
            super().__init__(title)
        else:
            raise IncorrectArgsException("The title is not valid")

    @staticmethod
    def is_valid(title):
        return re.fullmatch(r'[A-Za-z0-9 ]{,15}\b', title) is not None


class Content(Field):
    pass


class Tag(Field):
    pass


class Note:
    def __init__(self, content, title=None):
        self.content = Content(content)
        self.title = Title(title) if title else None
