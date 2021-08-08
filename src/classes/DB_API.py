from tests.integration.fixtures.people_data import sample_user_db


sample_db = [
    {
        'uname':'Behzad',
        'password':123
    },
    {
        'uname':'aaa',
        'password':125
    }
]

def creadential_in_db(db=None, uname=None, pw=None, ex_check=None):
    """[summary]

    Args:
        db ([type], optional): [description]. Defaults to None.
        uname ([type], optional): [description]. Defaults to None.
        pw ([type], optional): [description]. Defaults to None.
        ex_check ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    if db == None:
        print('\n\t[warning]: No database Found!! \n\t[warning]: Fake database is deploying...\n')
        db = sample_db
    for i, user_in_db in enumerate(sample_db):
        # check if credentials are valid against users database
        try:
            if uname == user_in_db['uname'] and int(pw) == user_in_db['password']:
                return True
        except:
        # check if user already existed
            if uname == user_in_db['uname'] and ex_check:
                print(uname)
                return True
            else:
                continue
    return False

def check_valid_access(uname, pw):
    valid_user_access = False

    # ToDo: check user against DB
    # ...
    valid_user_access = creadential_in_db(uname=uname, pw=pw)

    if valid_user_access == False:
        return False
    elif valid_user_access == True:
        return True

def check_user_existed(uname):
    user_existed = False

    # ToDo: check user against DB
    # ...
    user_existed = creadential_in_db(uname=uname, ex_check=True)

    if user_existed == False:
        return False
    elif user_existed == True:
        return True
    # check if new username does not exists in the database

def add_user_to_db(uname, pw):
    user_added = False
    
    # ToDo: CRUD - Create/ add user in DB
    # ...
    sample_db.append({'uname':uname, 'password':pw})
    user_added = True
    print("All Users:",[ user['uname'] for i, user in enumerate(sample_db)], end='\n')

    if user_added == True:
        return True
    elif user_added == False:
        return False