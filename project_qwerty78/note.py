from .field import Field


class Title:
    def __init__(self, title):
        self.title = title


class Content:
    def __init__(self, content):
        self.content = content


class Tag:
    pass  # No changes required for Tag class


class Note:
    def __init__(self, title, content):
        self.title = Title(title)
        self.content = Content(content)
