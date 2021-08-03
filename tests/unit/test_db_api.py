from src.classes.DB_API import check_user_existed, check_valid_access, add_user_to_db, creadential_in_db
from tests.integration.fixtures.people_data import sample_user_db 
def test_check_user_existed():
    assert check_user_existed(uname='aaa') == True

def test_check_valid_access():
    assert check_valid_access(uname='aaa', pw='125') == True


def test_add_user_to_db():
    assert add_user_to_db(uname='abram',pw='123') == True

def test_credential_in_db():
    assert creadential_in_db(db= sample_user_db, uname='aaa', pw='125') == True