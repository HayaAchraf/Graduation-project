import sqlite3

def create_tables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    
    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, 
            password TEXT, 
            role TEXT
        )
    """)
    
    # Images table
    c.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, 
            image_path TEXT,
            classification TEXT,
            timestamp TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def add_user(username, password, role="user"):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()