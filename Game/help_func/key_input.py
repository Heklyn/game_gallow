import pygame as pg

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
           'o', 'p', '[', ']', 'a', 's', 'd', 'f',
           'g', 'h', 'j', 'k', 'l', ';', "'", 'z',
           'x', 'c', 'v', 'b', 'n', 'm', ',', '.',
           'backspace'
]

russian_letters = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш',
                   'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А',
                   'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я',
                   'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю',
                   'backspace']


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
