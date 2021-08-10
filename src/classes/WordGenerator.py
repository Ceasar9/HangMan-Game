
class WordGenerator(object):
    def __init__(Self):
        pass

class FakeWordGenerator(object):
    def __init__(self):
        self.__gen_word = "HangMan Gamer"

    def set_gen_word(self, word=None):
        if word == None or not isinstance(word, str):
            self.__gen_word = "Simorgh"
        elif isinstance(word, str):
            self.__gen_word = word
    
    def get_gen_word(self):
        return self.__gen_word
