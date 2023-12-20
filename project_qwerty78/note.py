from .field import Field
import re
from .exceptions import IncorrectArgsException
from rich.table import Table
from rich.style import Style

def get_note_table():
    table = Table(show_lines=True)

    header_style = Style(bgcolor="rgb(201,58,57)")
    table_style = Style(color="rgb(255,255,255)", bgcolor="rgb(42,42,42)")
    for column in ["Index", "Title", "Content"]:
        table.add_column(column, header_style=header_style, style=table_style)

    return table


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

    def printable_view(self, table, index):
        table.add_row(
            str(index + 1), 
            str(self.title) if self.title else "", 
            str(self.content))
        
        return table

    def matches_title(self, query):
        """Повертає True, якщо запит знаходиться в заголовку нотатки."""
        return query.lower() in (self.title.value.lower() if self.title else '')

    def matches_content(self, query):
        """Повертає True, якщо запит знаходиться в змісті нотатки."""
        return query.lower() in self.content.value.lower()