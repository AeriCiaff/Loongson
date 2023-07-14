import sqlite3
import time

class DB:
    def __init__(self, database_file):
        self.database_file = database_file
        self.current_day = time.strftime("%Y_%m_%d")

    def insert_data(self, current_time, parameters_dict_str):
        try:
            with sqlite3.connect(self.database_file) as con:
                cur = con.cursor()
                cur.execute(f'''
                    CREATE TABLE IF NOT EXISTS {"_" + self.current_day} (
                    time TEXT,
                    parameters_dict TEXT
                );''')
                cur.execute(f"INSERT INTO {'_' + self.current_day}(time, parameters_dict) VALUES(?, ?)", (current_time, parameters_dict_str))
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            print(f"error:{current_time}\t{parameters_dict_str}")
    
    def fetch_all_data(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {'_' + self.current_day};")
                data = cur.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return
        return data
