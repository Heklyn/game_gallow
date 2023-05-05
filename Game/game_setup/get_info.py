from Game.game_setup.game_create import get_clock, get_screen
from Game.game_setup.config_reader import number_of_cells_in_weight


def get_center():
    size = get_screen().get_size()
    center = (round(size[0] / 2), round(size[1] / 2))

    return center


def get_background_info():
    num_x = number_of_cells_in_weight
    side_len = round(get_screen().get_size()[0] / num_x)
    num_y = round(get_screen().get_size()[1] / side_len)
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


def get_main_menu_button_masks():
    background_info = get_background_info()

    gap = round((background_info['num_y'] - 9) * background_info['side_len'] / 4)

    button_height = gap * 3 / 4
    button_width = 8 * background_info["side_len"]

    start_width = 11 * background_info['side_len']
    start_height = 5.5 * background_info['side_len']

    button_masks = []
    for i in range(5):
        button_masks.append({
            'size': (button_width, button_height),
            'coord': (start_width, start_height + i * gap)

        })

    return button_masks


def get_append_words_button_mask():
    background_info = get_background_info()

    gap = round((background_info['num_y'] - 9) * background_info['side_len'] / 4)

    button_height = gap * 3 / 4
    button_width = 12 * background_info["side_len"]

    start_width = 9 * background_info['side_len']
    start_height = 8.5 * background_info['side_len']

    button_masks = [{
        'size': ((button_width - gap) // 2, button_height),
        'coord': (start_width, start_height)
    },
        {
        'size': ((button_width - gap) // 2, button_height),
        'coord': (start_width + button_width + gap, start_height)
    },
        {
        'size': (button_width, button_height),
        'coord': (start_width, start_height + button_height + gap)
    }]
    return button_masks

