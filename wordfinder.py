from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = []
        self.word = ''
        self.read_list()

    def __repr__(self):
        return f"<WordFinder file_path={self.file_path}>"

    def random(self):
        self.word = choice(self.word_list)
        self.word = self.word.replace("\n", "")
        return self.word

    def read_list(self):
        f = open(self.file_path)
        self.word_list = f.readlines()
        print(f"{len(self.word_list)} words read")

class SpecialWordFinder(WordFinder):
    """ Special Word Finder: finds random words from a dictionary
    but omits blank lines and comments """
    def __init__(self)