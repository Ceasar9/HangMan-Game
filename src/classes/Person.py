from src.classes.DB_API import check_valid_access, check_user_existed


class Person(object):
    def __init__(self, uname):
        self.__username = ""
        self.__set_username(uname)

    def __set_username(self, uname):
        try:
            if isinstance(uname, str):
                self.__username = uname
        except TypeError:
            print("given username ist not a valid username")

    def get_username(self):
        return str(self.__username)
