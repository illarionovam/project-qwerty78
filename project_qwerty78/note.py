from .field import Field
import re
from .exceptions import IncorrectArgsException
from rich.table import Table

def get_note_table():
    table = Table(show_lines=True)

    table.add_column("Index", style="black on green")
    table.add_column("Title", style="magenta on cyan")
    table.add_column("Content", style="magenta")

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
