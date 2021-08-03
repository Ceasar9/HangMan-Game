import pytest

@pytest.fixture
def sample_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def sample_user_db():
    return [
        {
            'uname':'Behzad',
            'password':123
        },
        {
            'uname':'aaa',
            'password':125
        }
    ]