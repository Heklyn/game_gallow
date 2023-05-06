from Game.states.game_states import Game_scenarios, Playing_type
from Game.game_setup.game_create import start_game, close_game
from Game.scenarios import main_menu, append_words, choose_words_len, enter_word, playing

start_game()
state = Game_scenarios.main_menu


while state != Game_scenarios.exit_game:
    if state == Game_scenarios.main_menu:
        state, game_type = main_menu.play()

    elif state == Game_scenarios.playing:
        state = playing.play()

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




