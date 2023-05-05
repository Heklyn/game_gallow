import pygame as pg

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
           'o', 'p', '[', ']', 'a', 's', 'd', 'f',
           'g', 'h', 'j', 'k', 'l', ';', "'", 'z',
           'x', 'c', 'v', 'b', 'n', 'm', ',', '.']

russian_letters = [
    'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш',
    'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а',
    'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я',
    'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',
]


def is_accept_symbol(letter: str):
    if letter in letters:
        return True
    return False


def get_letter(symbol_code: int):
    symbol = pg.key.name(symbol_code)
    if is_accept_symbol(letter=symbol):
        letter = russian_letters[letters.index(symbol)]
        return letter
    return None
