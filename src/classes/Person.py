from src.classes.DB_API import check_valid_access, check_user_existed
class Person(object):
    def __init__(self, uname):
        self.username = ""
        self.set_username(uname)
    
    def set_username(self, uname):
        


        if isinstance(uname, str):
            self.username = uname
        else:
            print("given username ist not a valid username")