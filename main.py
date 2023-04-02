import sqlite3

db = sqlite3.connect("test.db")

# Create Cursor
cur = db.cursor()


def create_Character_Table():
    cur.execute(""" CREATE TABLE IF NOT EXISTS characters (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    VARCHAR(50) NOT NULL,
            hp      INT NOT NULL,
            atk     INT NOT NULL,
            def     INT NOT NULL,
            speed   INT NOT NULL 
        )""")
def data_entry_characters(name, hp, atk, defense, speed):
    cur.execute(f"""INSERT INTO characters (name,hp,atk,def,speed)
        VALUES ({name},{hp},{atk},{defense},{speed}) """)
    db.commit()
    cur.close()
    db.close()


data = [
    ("Jing Yuan", 1164, 698, 485, 99),
    ("Hook", 643, 546, 56464, 464),
    ("March 7th", 345, 666, 135, 444)
]
# проверка для теста что таблица создалась
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
