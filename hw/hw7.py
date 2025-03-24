import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users.db')

# Рука, которая держит ручку
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


# CRUD - Create - Read - Update - Delete


# CREATE
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен!")


# READ
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей")
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print('Пользователей нету!!')


# Функция для получения пользователя по rowid
def get_user_by_id(rowid):
    cursor.execute('SELECT rowid, * FROM users WHERE rowid = ?', (rowid,))
    user = cursor.fetchone()
    if user:
        print(f"NAME: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print(f'Пользователь с rowid {rowid} не найден!')


# UPDATE

def update_users(rowid, name=None, age=None, hobby=None):
    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if hobby is not None:
        fields.append("hobby = ?")
        values.append(hobby)

    if fields:
        query = f"UPDATE users SET {', '.join(fields)} WHERE rowid = ?"
        values.append(rowid)
        cursor.execute(query, values)
        connect.commit()
        print(f"Пользователь с rowid: {rowid} обновлен! {', '.join(fields)}")
    else:
        print("Нет данных для обновления!")


# DELETE
def delete_user(name):
    cursor.execute('DELETE FROM users WHERE name = ?',
                   (name,))
    connect.commit()
    print('Пользователь удален!!')


# add_user('Eldar', 22, 'swim')
