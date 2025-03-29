import sqlite3


def create_users_grades_view():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE VIEW IF NOT EXISTS users_grade AS
        SELECT users.user_id, users.name, users.age, users.hobby, grades.subject, grades.grade
        FROM users
        JOIN grades ON users.user_id = grades.user_id
    """)

    connection.commit()
    connection.close()


def get_young_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users_grade")
    results = cursor.fetchall()

    for row in results:
        print(row)

    connection.close()

create_users_grades_view()

get_young_users()
