
from src.app import *

if __name__=='__main__':
    usr_existed, usr_added, inp_usr = user_login_interface()
    game_loop(uname=inp_usr)