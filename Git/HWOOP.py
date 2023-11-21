# SQL - tasks
# Task 1. create table Person, with id: int, primary key, name: text, surname: text, date_of_birth date

import sqlite3
from faker import Faker

conn = sqlite3.connect('mydb.db')

print("DEB: Conn:", conn)

conn.execute('''CREATE TABLE IF NOT EXISTS
             person (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, date_of_birth DATE )''')

conn.commit()
conn.close()

# Task 2. Заповнити таблицю Person 15 кортежів (рядів), *use - faker, *use - context manager

fake = Faker()
Faker.seed(42)

conn = sqlite3.connect('mydb.db')

for i in range(1, 16):
    print("DEB: Add data:", i, fake.name(), fake.surname(), fake.date_of_birth)
    conn.execute("INSERT INTO person (id, name, surname, date_of_birth) VALUES (?, ?, ?, ?)",(i, fake.name(), fake.surname(), fake.date_of_birth))


conn.commit()
conn.close()

# Task 3. Знайти всіх людей у кого день народження 19-03-1998 або 12-10-1998

# Task 4. Знайте найстарших людей в наборі(топ 5)

# Task 5. Вивезти всіх у кого name більше surname

# * Оформити потрібно на гіт, з перевіркою flake8, requirements.txt, gitignore