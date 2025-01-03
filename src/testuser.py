import sqlite3

def create_test_user():
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    try:
        # Insert the test user
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('test', 'test'))
        conn.commit()
        print("User 'test' with password 'test' has been created successfully.")
    except sqlite3.IntegrityError:
        print("User 'test' already exists in the database.")
    finally:
        # Close the database connection
        conn.close()

if __name__ == '__main__':
    create_test_user()
