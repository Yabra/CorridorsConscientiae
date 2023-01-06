import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('points.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS points
                      (ID integer PRIMARY KEY ,
                       amount_of_points int)''')

    # метод добавления очков в таблицу
    # amount - кол-во очков, полученных за игру
    def add_points(self, amount):
        self.cur.execute(f'''INSERT INTO points(amount_of_points) VALUES({amount})''')
        self.con.commit()

    # удвление всего содержимого таблицы
    def delete_all_points(self):
        self.cur.execute('''DELETE from points''')

    # возвращает сумму очков
    def sum(self):
        st = list(self.cur.execute('''SELECT amount_of_points from points'''))
        total = sum(list(map(lambda x: x[0], st)))
        return total

    # возвращает сколько всего было попыток
    def total_attempts(self):
        st = list(self.cur.execute('''SELECT ID from points'''))
        total = list(map(lambda x: x[0], st))[-1]
        return total
