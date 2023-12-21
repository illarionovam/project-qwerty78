from .field import Field
import re
from .exceptions import IncorrectArgsException
from rich.table import Table
from rich.style import Style

def get_note_table():
    table = Table(show_lines=True)

    header_style = Style(bgcolor="rgb(201,58,57)")
    table_style = Style(color="rgb(255,255,255)", bgcolor="rgb(42,42,42)")
    for column in ["Index", "Title", "Tags", "Content"]:
        table.add_column(column, header_style=header_style, style=table_style)

    return table


class Title(Field):
    def __init__(self, title):
        if Title.is_valid(title):
            super().__init__(title)
        else:
            raise IncorrectArgsException("The title is not valid.")

    @staticmethod
    def is_valid(title):
        return re.fullmatch(r'[A-Za-z0-9 ]{,15}\b', title) is not None


class Content(Field):
    def __init__(self, content):
        """Checks is the content is not empty. 
        """
        if Content.is_valid(content):
            super().__init__(content)
        else:
            raise IncorrectArgsException("The content should not be empty.")

    @staticmethod
    def is_valid(name):
        return re.fullmatch(r".+", name) is not None


class Tag(Field):
    def __init__(self, tag):
        if not self.is_valid(tag):
            raise ValueError("Invalid tag. Tags must be alphanumeric and up to 10 characters long.")
        super().__init__(tag.lower())

    @staticmethod
    def is_valid(tag):
        '''Check for alphanumeric characters, length constraint, and no spaces'''
        return re.fullmatch(r'[A-Za-z0-9]{1,10}', tag) is not None and ' ' not in tag


class Note:
    def __init__(self, content, title=None):
        self.content = Content(content)
        self.title = Title(title) if title else None
        self.tags = set()   # Using a set to store unique tags

    def printable_view(self, table, index):
        table.add_row(
            str(index + 1), 
            str(self.title) if self.title else "",
            ', '.join(self.tags) if self.tags else "", 
            re.sub("\[", "\\[", str(self.content)))
        
        return table

    def matches_title(self, query):
        """Returns True, if query is a part of the note's title."""
        return query.lower() in (self.title.value.lower() if self.title else '')


    def matches_content(self, query):
        """Returns True, if query is a part of the note's content."""
        return query.lower() in self.content.value.lower()


    def add_tag(self, tag):
        new_tag = Tag(tag)                      # Creates a Tag object that performs validation
        if new_tag.value in self.tags:          # Check if the tag exists
            raise ValueError(f"Tag '{tag}' already exists in this note.")
        self.tags.add(new_tag.value)

    def remove_tag(self, tag):
        normalized_tag = Tag(tag).value         # Tag normalization
        if normalized_tag not in self.tags:     # Check if the tag exists
            raise ValueError(f"Tag '{tag}' does not exist in this note.")
        self.tags.discard(normalized_tag)