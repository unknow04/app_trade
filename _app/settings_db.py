import sqlite3 as sq

query_setting = """CREATE TABLE IF NOT EXISTS settings(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                       host VARCHAR, port VARCHAR);"""


class SettingData:
    def __init__(self):
        self.conn = sq.connect("../database/settings_db.db")
        self.cur = self.conn.cursor()
        self.cur.execute(query_setting)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def delete_data(self):
        self.cur.execute("""DELETE FROM settings;""")
        self.conn.commit()

    def get_data(self):
        data = self.cur.execute("""SELECT * FROM settings;""")
        data = data.fetchone()
        return data

    def save_data(self, *args):
        try:
            self.delete_data()
        except:
            pass
        self.cur.execute("""INSERT INTO settings(host, port) VALUES(?, ?);""", args)
        self.conn.commit()


if __name__ == '__main__':
    db = SettingData()
    db.save_data("128.0.0.1", 5003)
    db.get_data()
