from Game.help_func.filters import is_word_correct
from Game.states.game_states import Word_code, File_code


class Txt_reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        status = File_code.Ok
        try:
            self.file = open(self.file_name, "r", encoding="utf-8")
        except Exception:
            status = File_code.Not_exist
        return status

    def get_word(self):
        try:
            word = self.file.readline()[:-1].upper()
            while not is_word_correct(word):
                word = self.file.readline()[:-1].upper()
                if not word:
                    raise Exception
        except Exception:
            return Word_code.Not_get, None
        return Word_code.Ok, word

    def close_file(self):
        self.file.close()