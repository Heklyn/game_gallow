import configparser


def create_user_config():
    config = configparser.ConfigParser()

    config['MAIN_SETTINGS'] = {
        'fps': '60',
    }
    config['player_score'] = {
        'game': '0',
        'win': '0',
        'lose': '0'
    }
    with open('config.ini', 'w') as config_file:
        config.write(config_file)


def create_system_config():
    config = configparser.ConfigParser()

    config['MAIN_SETTINGS'] = {
        'min_word_len': '6',
        'max_word_len': '13',
        'number of cells in weight': '30',
        'button_width': '0.3985',
        'button_height': '0.10',
        'gap': '0.01',

    }

    with open('Game/game_setup/system_config.ini', 'w') as config_file:
        config.write(config_file)


def read_user_config():
    global fps, game, win, lose
    fps = int(user_config.get('MAIN_SETTINGS', 'fps'))
    game = int(user_config.get('player_score', 'game'))
    win = int(user_config.get('player_score', 'win'))
    lose = int(user_config.get('player_score', 'lose'))


def read_system_config():
    global number_of_cells_in_weight, min_word_len, max_word_len, button_width, button_height, gap
    number_of_cells_in_weight = int(system_config.get('MAIN_SETTINGS', 'number of cells in weight'))

    min_word_len = int(system_config.get('MAIN_SETTINGS', 'min_word_len'))
    max_word_len = int(system_config.get('MAIN_SETTINGS', 'max_word_len'))

    button_width = float(system_config.get('MAIN_SETTINGS', 'button_width'))
    button_height = float(system_config.get('MAIN_SETTINGS', 'button_height'))
    gap = float(system_config.get('MAIN_SETTINGS', 'gap'))


def get_stats():
    read_user_config()
    return game, win, lose


def update_score(is_win: bool):
    game, win, lose = get_stats()
    if is_win:
        user_config.set('player_score', 'win', f"{win + 1}")
    else:
        user_config.set('player_score', 'lose', f"{lose + 1}")

    user_config.set('player_score', 'game', f"{game + 1}")

    with open('config.ini', 'w') as config_file:
        user_config.write(config_file)


user_config = configparser.ConfigParser()
system_config = configparser.ConfigParser()

try:
    system_config.read('Game/game_setup/system_config.ini')
    read_system_config()
except Exception:
    create_system_config()
    system_config.read('Game/game_setup/system_config.ini')
    read_system_config()

try:
    user_config.read('config.ini')
    read_user_config()
except Exception:
    create_user_config()
    user_config.read('config.ini')
    read_user_config()
