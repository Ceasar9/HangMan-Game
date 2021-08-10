from src.app import user_login_interface
import pytest
# import mock
# import builtins
from io import StringIO

def test_integration_mocktest_user_login_interface(monkeypatch):
    
    user_inputs = StringIO('n\nBehzad\n123\n')
    # ToDo integration Test  - Mock-Test (for user-input)
    # ...
    monkeypatch.setattr('sys.stdin', user_inputs)
    assert user_login_interface() == [True, False, 'Behzad']


# def test_integration_mocktest_user_login_interface(monkeypatch):
#     user_inputs = StringIO('y\nBehzad\n123\n')
 
#     # ToDo integration Test  - Mock-Test (for user-input)
#     # ...
#     monkeypatch.setattr('sys.stdin', user_inputs)
#     assert user_login_interface() == None

def test_integration_mocktest_user_login_interface_new_user(monkeypatch):
    user_inputs = StringIO('y\naa\n123\n')
    # ToDo integration Test  - Mock-Test (for user-input)
    # ...
    monkeypatch.setattr('sys.stdin', user_inputs)
    assert user_login_interface() == [False, True, 'aa']