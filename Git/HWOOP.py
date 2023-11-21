import sqlite3
from faker import Faker
import time

# Декоратори
# Task 1. Реалізуйте декоратор type_check,
# який перевіряєвідповідність типів аргументів функції заданим типам і викидає виняток, якщо типи не збігаються.

import time
def type_check(*required_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if not isinstance(args[i], required_types[i]):
                    raise TypeError(f" Очікували {required_types[i]}, однак отримали {type(args[i])}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Використання

@type_check(int, str)
def my_function(num, text):
    print(f'це число: {num}, це текст: {text}')

my_function(42, "Hello")

# Task 2. Реалізуйте декоратор delay, який затримує виконання функції на вказану кількість секунд.
# Функція повинна на заданий час давати shutdown, також повинна бути перевірка на статус код та try/except для перевірки connection

# SQL - tasks
# Task 1. create table Person, with id: int, primary key, name: text, surname: text, date_of_birth date

conn = sqlite3.connect('mydb.db')

print("DEB: Conn:", conn)

conn.execute('''CREATE TABLE IF NOT EXISTS
             person (id INTEGER PRIMARY KEY, name TEXT, user_name TEXT, date_of_birth DATE )''')

conn.commit()
conn.close()

# Task 2. Заповнити таблицю Person 15 кортежів (рядів), *use - faker, *use - context manager

fake = Faker()
Faker.seed(42)

conn = sqlite3.connect('mydb.db')

for i in range(1, 16):
    print("DEB: Add data:", i, fake.name(), fake.user_name(), fake.date_of_birth())
    conn.execute("INSERT INTO person (id, name, user_name, date_of_birth) VALUES (?, ?, ?, ?)",(i, fake.name(), fake.user_name(), fake.date_of_birth()))

conn.commit()
conn.close()

# Task 3. Знайти всіх людей у кого день народження 19-03-1998 або 12-10-1998

conn = sqlite3.connect('mydb.db')

cursor = conn.execute("SELECT id, name, date_of_birth FROM person WHERE date_of_birth IN ('1984-08-05','1992-06-19')")
rows = cursor.fetchall()

for row in rows:
    print("DEB: Task 3:", row)

conn.close()

# Task 4. Знайте найстарших людей в наборі(топ 5)

conn = sqlite3.connect('mydb.db')

cursor = conn.execute("SELECT id, name, date_of_birth FROM person ORDER BY date_of_birth ASC")

rows = cursor.fetchmany(5)
for row in rows:
    print("DEB: Task 4:", row)

# Task 5. Вивезти всіх у кого name більше surname

conn = sqlite3.connect('mydb.db')

cursor = conn.execute("SELECT name FROM person")
rows = cursor.fetchall()

for row in rows:
    # print("DEB1: Task 4:", row)
    names_list = row[0].split(' ')
    if len(names_list[0]) > len(names_list[1]):
        print("DEB2: Task 4.1:", names_list)

# * Оформити потрібно на гіт, з перевіркою flake8, requirements.txt, gitignore