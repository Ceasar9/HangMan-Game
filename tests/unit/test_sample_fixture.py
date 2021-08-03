#%%
from tests.integration.fixtures.people_data import sample_people_data
# from ..conftest import *
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import format_data_for_display
#%%
print(sys.path)
def test_input():
    string = "behzad"
    assert isinstance(string, str)
        



def test_format_data_for_display(sample_people_data):
    assert format_data_for_display(sample_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


# format_data_for_display([
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ])
# %%
