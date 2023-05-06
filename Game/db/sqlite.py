import sqlite3 as sq


def db_start():
    global db, cur

    db = sq.connect('bot_db.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Words(word_id INTEGER PRIMARY KEY, word TEXT, word_len INTEGER)")
    db.commit()


def create_word(word: str):
    cur.execute("INSERT INTO Words VALUES(?, ?, ?)",
                (None, word, len(word)))
    db.commit()


def get_word(word_id: int):
    value = cur.execute(f"SELECT word FROM Words WHERE word_id == {word_id}").fetchone()
    return value


def is_word_in_db(word: str):
    value = cur.execute(f"SELECT word FROM Words WHERE word == '{word}'").fetchall()
    if value:
        return True
    return False