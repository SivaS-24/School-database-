import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('school.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        sno INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        sex TEXT,
        class TEXT,
        fees TEXT,
        rank INTEGER,
        english_mark INTEGER,
        python_mark INTEGER,
        math_mark INTEGER,
        class_teacher TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        sno INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        sex TEXT,
        salary INTEGER,
        class_teacher_class TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS principal (
        sno INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        sex TEXT,
        salary INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
        sno INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')

# Commit the changes
connection.commit()

