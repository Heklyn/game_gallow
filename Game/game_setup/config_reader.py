import configparser

user_config = configparser.ConfigParser()
user_config.read('config.ini')
system_config = configparser.ConfigParser()
system_config.read('Game/game_setup/system_config.ini')

fps = int(user_config.get('MAIN_SETTINGS', 'fps'))
number_of_cells_in_weight = int(system_config.get('MAIN_SETTINGS', 'number of cells in weight'))

min_word_len = int(system_config.get('MAIN_SETTINGS', 'min_word_len'))
max_word_len = int(system_config.get('MAIN_SETTINGS', 'max_word_len'))

button_width = float(system_config.get('MAIN_SETTINGS', 'button_width'))
button_height = float(system_config.get('MAIN_SETTINGS', 'button_height'))
gap = float(system_config.get('MAIN_SETTINGS', 'gap'))
