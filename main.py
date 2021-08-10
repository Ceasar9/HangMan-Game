
from src.app import *
import os

if __name__=='__main__':
    os.system('clear')
    usr_existed, usr_added, inp_usr = user_login_interface()
    game_loop(uname=inp_usr)