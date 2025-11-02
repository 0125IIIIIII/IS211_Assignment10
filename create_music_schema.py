import sqlite3
# Connect to (or create) the SQLite database
conn = sqlite3.connect('music.db')
cursor = conn.cursor()
# Create Artist table
cursor.execute('''
CREATE TABLE IF NOT EXISTS artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Create Album table
cursor.execute('''
CREATE TABLE IF NOT EXISTS album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
)
''')

# Create Song table
cursor.execute('''
CREATE TABLE IF NOT EXISTS song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    duration_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id)
)
''')

# Commit changes and close connection
conn.commit()
conn.close()
print("Music schema created successfully in music.db")
