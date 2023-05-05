from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.get_info import get_append_words_button_mask
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.graphic_elements.logo import create_logo
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios
from Game.game_setup.config_reader import fps
from Game.scenarios.get_event import event


def create_screen_detail():
    surf = create_background()
    logo, logo_coord = create_logo()
    surf.blit(logo, logo_coord)

    buttons = []

    button_texts = ['Не подходит', 'Подходит', 'Главное меню']
    button_states = [Button_data.skip, Button_data.accept, Button_data.return_menu]
    button_masks = get_append_words_button_mask()
    buttons_type = [Button_type.Playing, Button_type.Playing, Button_type.Scenario]

    for mask, text, callback_data in zip(button_masks, button_texts, button_states):
        if callback_data == Button_data.return_menu:
            type = Button_type.Scenario
        else:
            type = Button_type.Playing

        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     type=type))

    return surf, buttons


def game_loop():
    screen = get_screen()
    clock = get_clock()

    surf, buttons = create_screen_detail()
    screen.blit(surf, (0, 0))

    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        event_type, event_data = event(surf=screen, buttons=buttons)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game
        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu

