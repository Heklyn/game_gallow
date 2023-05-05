from Game.states.game_states import Game_scenarios
from Game.game_setup.game_create import start_game, close_game
from Game.scenarios import main_menu

start_game()
state = Game_scenarios.main_menu


while state != Game_scenarios.exit_game:
    if state == Game_scenarios.main_menu:
        state, game_type = main_menu.play()
    elif state == Game_scenarios.playing:
        pass
    elif state == Game_scenarios.enter_word:
        pass
    elif state == Game_scenarios.choose_words_len:
        pass
    elif state == Game_scenarios.append_words:
        pass


close_game()

