def wrap_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        #TODO: add exceptions processing here
        except IndexError as e:
            return "Index out of range."
        except Exception as e:
            return e

    return inner