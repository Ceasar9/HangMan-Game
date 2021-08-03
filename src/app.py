from src.classes.DB_API import add_user_to_db, check_valid_access, check_user_existed
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

from src.classes.Person import Person

def game_loop(uname=None):
    player = Person(uname)