from Game.db import sqlite
from Game.game_setup.config_reader import min_word_len, max_word_len
from Game.help_func.key_input import is_russian_word


def is_word_correct(word: str):
    if not word.isalpha():
        return False

    if not min_word_len <= len(word) <= max_word_len:
        return False

    if sqlite.is_word_in_db(word):
        return False

    if not is_russian_word(word):
        return False

    return True
