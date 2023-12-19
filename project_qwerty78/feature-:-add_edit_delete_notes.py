

class AddressBook:
    def __init__(self):
        self.notes = [] 

    def wrap_exception(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IndexError as e:
                raise WrapException(f"Index out of range: {e}")
        return inner

    @wrap_exception
    def add_note(self, title, content):
        self.notes.append(Note(title, content))

    @wrap_exception
    def delete_note_by_index(self, index):
        del self.notes[index]

    @wrap_exception
    def edit_note_by_index(self, index, title, content):
        self.notes[index].title = title
        self.notes[index].content = content
