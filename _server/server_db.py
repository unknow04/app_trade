import sqlite3 as sq

query_user = """CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                first_name VARCHAR,
                                                last_name VARCHAR,
                                                password VARCHAR,
                                                email VARCHAR NOT NULL UNIQUE,
                                                age INTEGER,
                                                is_active INTEGER DEFAULT 0,
                                                is_super INTEGER DEFAULT 0);"""


class User:
    def __init__(self):
        self.conn = sq.connect("../database/user_db.db")
        self.cur = self.conn.cursor()
        self.cur.execute(query_user)
        self.conn.commit()

    def registration_user(self, *args):
        self.cur.execute("""INSERT INTO user(first_name, last_name, password, email, age) VALUES(?, ?, ?, ?, ?);""",
                         args)
        self.conn.commit()

    def show_name(self):
        data_name = self.cur.execute("""PRAGMA table_info(user);""")
        data_name, names = data_name.fetchall(), []
        for h in data_name:
            names.append(h[1])
        return names

    def connect_user(self, **kwargs):

        user_data = self.cur.execute(f"""SELECT * FROM user WHERE email='{kwargs['email']}';""")
        data = user_data.fetchone()
        if data[3] == kwargs['password']:
            data = dict(zip(self.show_name(), data))
            return data


if __name__ == '__main__':
    user = User()
    user.registration_user("sfdfs", "fdsfds", "fssf44", "fdsffdsf", "fds")
