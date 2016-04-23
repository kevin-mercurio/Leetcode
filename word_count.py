

class WordCount:

    def __init__(self, in_str):
        self.freq_dict = {}
        self.prep_words_and_count(in_str)

    def prep_words_and_count(self, in_str):
        words = in_str.split()
        print words

    def add_to_dict(self, word):
        self.freq_dict[word] = 1


