from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = []
        self.word = ''
        self.read_list()

    def __repr__(self):
        """Updated repr"""
        return f"<WordFinder file_path={self.file_path}>"

    def random(self):
        """Returns random word from word list"""
        self.word = choice(self.word_list)
        self.word = self.word.replace("\n", "")
        return self.word

    def read_list(self):
        """Reads file and creates list of lines"""
        f = open(self.file_path)
        self.word_list = f.readlines()
        print(f"{len(self.word_list)} words read")

class SpecialWordFinder(WordFinder):
    """ Special Word Finder: finds random words from a dictionary
    but omits blank lines and comments """

    def __init__(self,file_path):
        super().__init__(file_path)

    
    def read_list(self):
        """Manually loops over file to remove comments and blank lines
        Returns list of lines"""
        f = open(self.file_path)

        for line in f:
            if not line.startswith("#") and not line.startswith("\n"):
                self.word_list.append(line)

        print(f"{len(self.word_list)} words read")
