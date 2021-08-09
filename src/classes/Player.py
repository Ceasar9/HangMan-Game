from src.classes.DB_API import check_valid_access, check_user_existed

from src.classes.Person import Person

class Player(Person):
    def __init__(self, uname, pl_name=None, word_length=0):
        super().__init__(uname=uname) 

        self.__player_name = pl_name
        self.__current_guess = None
        self.__gussed_letters = []
        self.__total_chacnes = word_length
        self.__remained_chances = self.__total_chacnes

        self._set_player_name(pl_name)


    def _set_player_name(self, pl_name):
        try:
            if isinstance(pl_name, str):
                self.__player_name = pl_name
        except TypeError:
            print('please enter text as your name ...')

    def get_player_name(self):
        return self.__player_name

    def set_current_guess(self, guessed_letter=None, correct_guess=None):
        if isinstance(guessed_letter, str):
            if guessed_letter in self.__gussed_letters:
                print('Already taken, pick a new charactre!') 
            elif len(guessed_letter) != 1:
                print('Please enter one character per round. Entered: {}'.format(guessed_letter))
            elif len(guessed_letter) == 1:
                self.__current_guess = guessed_letter
                self.__set_guessed_letterss(guessed_letter)
                self._set_ramained_chances(correct_guess= correct_guess)

    def get_current_guess(self):
        return self.__current_guess

    def __set_guessed_letterss(self, guessed_letter):
        self.__gussed_letters.append(guessed_letter)

    def get_guessed_letter(self):
        return self.__gussed_letters

    def _set_ramained_chances(self, correct_guess= None):

        if correct_guess != None and correct_guess == False:
            self.__remained_chances -= 1
        if self.__remained_chances == 0:
            return "GAME OVER"
            

    def get_remianed_chances(self):
        return self.__remained_chances
