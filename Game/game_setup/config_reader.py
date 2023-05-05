import configparser

user_config = configparser.ConfigParser()
user_config.read('config.ini')
system_config = configparser.ConfigParser()
system_config.read('Game/game_setup/system_config.ini')

fps = int(user_config.get('MAIN_SETTINGS', 'fps'))
number_of_cells_in_weight = int(system_config.get('MAIN_SETTINGS', 'number of cells in weight'))

button_width = int(system_config.get('MAIN_SETTINGS', 'button_width'))
button_height = int(system_config.get('MAIN_SETTINGS', 'button_height'))