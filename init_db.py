import sqlite3
import bcrypt
import os
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

def initialize_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password_hash TEXT NOT NULL,
                  role TEXT DEFAULT 'user',
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    # Check if CREATE_TEST_USER is set in the .env file
    if os.getenv("CREATE_TEST_USER") == "1":
        password = "admin123"
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            c.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                      ('admin', hashed_pw, 'admin'))
            print("Created test admin user")
        except sqlite3.IntegrityError:
            print("Admin user already exists")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully")
