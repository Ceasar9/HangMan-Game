import pytest
from src.classes.WordGenerator import FakeWordGenerator
def test_fake_word_gen_instantiate():
    fakeWordGen = FakeWordGenerator()
    assert type(fakeWordGen) == type(FakeWordGenerator())
    
def test_set_get_gen_word():
    fakeWordGen = FakeWordGenerator()
    assert fakeWordGen.get_gen_word() == 'HangMan Gamer'
    
    fakeWordGen.set_gen_word()
    assert fakeWordGen.get_gen_word() == 'Simorgh'
    
    fakeWordGen.set_gen_word(word='Sohrab')
    assert fakeWordGen.get_gen_word() == 'Sohrab'
