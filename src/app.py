from typing import Counter
from src.classes.DB_API import add_user_to_db, check_valid_access, check_user_existed

from src.classes.Player import Player
from src.classes.WordGenerator import FakeWordGenerator
import os
import re

def format_data_for_display(sample_people_data):
    new_list = []
    for i, data in enumerate(sample_people_data):
        print(i, data)
        new_list.append(data['given_name'] + " " + data['family_name'] + ": " + data['title'])
    # print(new_list)
    return new_list

def user_login_interface():
    while True:
            usr_existed = True
            usr_added = False
            new_user= input("new user?(y/yes, n/no):")
            if new_user in ['y','yes']:
                inp_uname = input('enter your new username:')
                pw = input('input your password:')
                usr_existed = check_user_existed(uname=inp_uname)
                if usr_existed == True:
                    print('Username already existed...')
                    continue
                elif usr_existed == False:
                    print('\tHi {}, welcome to Hangman! :D\n'.format(inp_uname))
                    usr_added = add_user_to_db(uname=inp_uname, pw=pw)
                    break     

            elif new_user in ['n', 'no']:
                inp_uname = input('enter your username:')
                pw = input('input your password:')
                valid_access = check_valid_access(uname=inp_uname, pw=pw)
                if valid_access == True:
                    print('Hi {}, Welcome Back to Hangman! :D\n'.format(inp_uname))
                    break
                if valid_access == False:
                    print('Error: Username or Password is not correct...!\n')
                    continue
    return [usr_existed, usr_added, inp_uname]

def game_loop(uname=None):
    wordgen = FakeWordGenerator()
    secret_word= str(wordgen.get_gen_word()).upper()
    player = Player(uname= uname, word_length=len(secret_word))
    correct_guess_flag = None
    display_board = [c if c == ' ' else '-' for c in secret_word ]
    correct_guess_list = []
    count = -1
    num_wrong_guessed = 0
    wrong_guess_list=[]
    usr_guess = ""
    input('Press Enter to Start the Game...')
    os.system('clear')
    while player.get_remianed_chances() > 0:
        if count == 0:
            usr_guess = input('\n Please Enter your first guess [a-z]:')
        elif count > 0:
            usr_guess = input('\nPlease Enter your next guess [a-z]:')
        os.system('clear')
        usr_guess = str(usr_guess).upper()
        if (re.match(r'[a-zA-Z]', usr_guess)) and (usr_guess not in wrong_guess_list) and (usr_guess not in correct_guess_list):
            if usr_guess in secret_word:
                correct_guess_flag = True
                player.set_current_guess(guessed_letter=usr_guess, correct_guess=correct_guess_flag)
                correct_guess_list.append(usr_guess)
            
            elif usr_guess not in secret_word:
                correct_guess_flag = False
                player.set_current_guess(guessed_letter=usr_guess, correct_guess=correct_guess_flag)
                num_wrong_guessed = len(secret_word) - player.get_remianed_chances()
                wrong_guess_list.append(usr_guess)

            if len(usr_guess) == 1 and isinstance(usr_guess, str):
                all_indices = [x.start() for x in re.finditer(usr_guess, secret_word)]
                for i in range(len(secret_word)):
                    if i in all_indices:
                        display_board[i] = usr_guess
      
        correct_guess_flag = None
        count+=1
        print('Guess-{} Finished...'.format(count))
        print('Guessed Letters:{}'.format(player.get_guessed_letter()))
        print('Chances left: {}'.format(player.get_remianed_chances()))
        print('\n\n|-------------|\n| BOARD GAME: | \n|-------------|\n\n ***{}***\n\n============\n\n'.format(''.join(display_board)))
        
        if '-' not in ''.join(display_board) and ''.join(display_board) == secret_word:
            print('Wiiiiiiiiiiiiiiiin!!! :D\n\n')
            break
        if num_wrong_guessed == len(secret_word):
            print('GameOver')
            break
        
