from Game.states.game_states import Game_scenarios, Playing_type
from Game.game_setup.game_create import start_game, close_game
from Game.scenarios import main_menu, append_words, choose_words_len, enter_word, playing
from Game.db.sqlite import get_word_with_fixed_length, get_word

start_game()
state = Game_scenarios.main_menu


while state != Game_scenarios.exit_game:
    if state == Game_scenarios.main_menu:
        state, game_type = main_menu.play()

    elif state == Game_scenarios.playing:
        if game_type == Playing_type.fast_play:
            word = get_word()
        elif game_type == Playing_type.with_fixed_length:
            word = get_word_with_fixed_length(word_len=word_len)
        state = playing.play(word=word)

    elif state == Game_scenarios.enter_word:
        state, word = enter_word.play()
        if state == Game_scenarios.playing:
            game_type = Playing_type.play_with_given_word

    elif state == Game_scenarios.choose_words_len:
        state, word_len = choose_words_len.play()
        if state == Game_scenarios.playing:
            game_type = Playing_type.with_fixed_length

    elif state == Game_scenarios.append_words:
        state, game_type = append_words.play()


close_game()




