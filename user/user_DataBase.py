import sqlite3


class Connect:
    def __init__(self):
        self.db = sqlite3.connect('settings.db')
        self.cur = self.db.cursor()

    def register(self, user_id, user_name):
        self.cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_id INTEGER UNIQUE, user_name TEXT)')
        self.cur.execute('INSERT INTO users (user_id, user_name) VALUES (?,?)', (user_id, user_name))
        self.db.commit()
