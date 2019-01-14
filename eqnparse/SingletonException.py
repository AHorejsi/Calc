class SingletonException(Exception):
    def __init__(self, type):
        self.message = str(type) + " is a singleton class"
