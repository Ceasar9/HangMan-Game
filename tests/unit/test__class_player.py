from src.classes.Player import Player
import pytest


def test_set_username():
    # test __set_username() on object instantiation
    player = Player(uname='Rostam-7')
    assert player.get_username() == 'Rostam-7'

    # check private __set_username() method
    # behavior against invalid public access
    try:
        player.__set_username('Rostam-6')
    except:
        pass
    assert player.get_username() == 'Rostam-7'


def test_get_username():
    player = Player(uname='Zal')
    assert player.get_username() == 'Zal'


# ToDo
def test_set_get_player_name():
    # test set/get by object instantiation
    player = Player(uname='Rostam-7', pl_name='Rostam Zaal')
    assert player.get_player_name() == 'Rostam Zaal'

    # test set/get after object instantiation
    player._set_player_name('Rostam Tahmine')
    assert player.get_player_name() == 'Rostam Tahmine'


def test_set_get_current_guess():
    # test set/get by object instantiation
    player = Player(uname='Rostam-7')
    assert player.get_current_guess() == None

    # test set/get after object instantiation
    player.set_current_guess(guessed_letter='s')
    assert player.get_current_guess() == 's'


def test_set_get_guessed_letters():
    player = Player(uname="Rostam-7")
    # set_guessed_letter internally right after current_guess is set.
    player.set_current_guess(guessed_letter='s')
    assert player.get_guessed_letter() == ['s']

    # test set_guessed_letter after entering second guess
    player.set_current_guess(guessed_letter='a')
    assert player.get_guessed_letter() == ['s', 'a']

    # test entering multiple guess
        # with pytest.raises(ValueError, match=r".*enter one character.*"):
    player.set_current_guess(guessed_letter='sb')
    assert player.get_guessed_letter() == ['s', 'a']


def test_set_get_remained_chances():
    # test remained number of chances after wrong first guess with give word_lenght
    player = Player(uname="Rostam-7", word_length=10)
    player.set_current_guess(guessed_letter='s', correct_guess=False)
    assert player.get_remianed_chances() == 9
    # test remained number of chances after correct second guess with give word_lenght
    player.set_current_guess(guessed_letter='b', correct_guess=True)
    assert player.get_remianed_chances() == 9

    # test remained number of chances after invalid guess with give word_lenght
        # with pytest.raises(ValueError, match=r".*enter one character.*"):
    player.set_current_guess(guessed_letter='sb')
    assert player.get_remianed_chances() == 9
