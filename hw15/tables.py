import sqlite3 as db

with db.connect('bookstore') as bs:
    cursor = bs.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'first_name TEXT NOT NULL,'
                   'last_name TEXT NOT NULL,'
                   'age INTEGER NOT NULL,'
                   'books_id INTEGER NOT NULL,'
                   'FOREIGN KEY (books_id) REFERENCES books (id)'
                   ')')

    cursor.execute('CREATE TABLE IF NOT EXISTS publishing_house ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'name TEXT NOT NULL,'
                   'rating INTEGER NOT NULL DEFAULT 5'
                   ')')

    cursor.execute('CREATE TABLE IF NOT EXISTS books ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'title TEXT NOT NULL,'
                   'author TEXT NOT NULL,'
                   'year INTEGER NOT NULL,'
                   'price INTEGER NOT NULL,'
                   'publishing_house_id INTEGER NOT NULL,'
                   'FOREIGN KEY (publishing_house_id) REFERENCES publishing_house (id)'
                   ')')

    cursor.execute('CREATE TABLE IF NOT EXISTS purchases ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'user_id INTEGER NOT NULL,'
                   'book_id INTEGER NOT NULL,'
                   'date INTEGER NOT NULL,'
                   'users_id INTEGER NOT NULL,'
                   'FOREIGN KEY (users_id) REFERENCES users (id)'
                   ')')
