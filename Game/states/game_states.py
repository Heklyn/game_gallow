from enum import Enum


class Game_scenarios(Enum):
    main_menu = 0
    playing = 1
    choose_words_len = 2
    enter_word = 3
    append_words = 4
    exit_game = 5


class Button_data(Enum):
    return_menu = 0
    exit_game = 1
    fast_play = 2
    play_with_fixed_length = 3
    play_with_given_word = 4
    add_word_to_db = 5
    length_plus = 6
    length_minus = 7
    accept = 8
    skip = 9


class Button_type(Enum):
    Scenario = 0
    Playing = 1


class Event_type(Enum):
    Not_event = 0
    Button = 1
    Quit = 2
    Key_press = 3


class Playing_type(Enum):
    fast_play = 0
    with_fixed_length = 1
    play_with_given_word = 2

