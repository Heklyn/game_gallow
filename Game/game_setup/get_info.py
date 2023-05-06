from Game.game_setup.game_create import get_clock, get_screen
from Game.game_setup import config_reader


def get_center():
    size = get_screen().get_size()
    center = (round(size[0] / 2), round(size[1] / 2))

    return center


def get_background_info():
    num_x = config_reader.number_of_cells_in_weight
    side_len = get_screen().get_size()[0] // num_x
    num_y = get_screen().get_size()[1] // side_len
    info = {
        'num_x': num_x,
        'num_y': num_y,
        'side_len': side_len,
    }

    return info


def get_logo_info():
    background_info = get_background_info()
    logo_info = {
        'size': (background_info['side_len'] * 18, background_info['side_len'] * 3),
        'coord': (background_info['side_len'] * 6, background_info['side_len'] * 1),
    }

    return logo_info


def get_button_sizes():
    screen_size = get_screen().get_size()
    button_width = config_reader.button_width * screen_size[0]
    button_height = config_reader.button_height * screen_size[1]
    gap = config_reader.gap * screen_size[0]
    button_width_small = (button_width - gap) // 2

    return button_width, button_width_small, button_height, gap


def get_start_pos_button(lower: bool = False):
    button_width, gap = get_button_sizes()[::2]
    screen_size = get_screen().get_size()
    start_width = screen_size[0] // 2 - button_width // 2 - 3
    if lower:
        start_height = screen_size[1] * 0.62
    else:
        start_height = screen_size[1] * 0.35

    return start_width, start_height


def create_button_masks(start_pos: tuple, list_button_count: tuple):
    button_width, button_width_small, button_height, gap = get_button_sizes()
    button_masks = []
    for line, count in enumerate(list_button_count):
        if count == 1:
            button_masks.append({
                'size': (button_width, button_height),
                'coord': (start_pos[0], start_pos[1] + line * button_height + line * gap)

            })
        if count == 2:
            button_masks.append({
                'size': (button_width_small, button_height),
                'coord': (start_pos[0], start_pos[1] + line * button_height + line * gap)
            })
            button_masks.append({
                'size': (button_width_small, button_height),
                'coord': (start_pos[0] + button_width // 2 + gap // 2, start_pos[1] + line * button_height + line * gap)
            })

    return button_masks


def get_main_menu_button_masks():
    start_width, start_height = get_start_pos_button()

    button_masks = create_button_masks(
        start_pos=(start_width, start_height),
        list_button_count=(1, 1, 1, 1, 1)
    )

    return button_masks


def get_append_words_button_mask():
    start_pos = get_start_pos_button(lower=True)

    button_masks = create_button_masks(
        start_pos=start_pos,
        list_button_count=(2, 1)
    )

    return button_masks


def get_choose_word_len_button_mask():
    start_pos = get_start_pos_button(lower=True)

    button_masks = create_button_masks(
        start_pos=start_pos,
        list_button_count=(1, 2, 1)
    )

    return button_masks


def get_enter_word_button_mask():
    start_pos = get_start_pos_button(lower=True)

    button_masks = create_button_masks(
        start_pos=start_pos,
        list_button_count=(1, 1)
    )

    return button_masks


def get_playing_button_mask():
    start_pos = get_start_pos_button(lower=True)

    button_masks = create_button_masks(
        start_pos=start_pos,
        list_button_count=(1, )
    )

    return button_masks


