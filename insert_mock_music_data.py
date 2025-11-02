import sqlite3

conn = sqlite3.connect('music.db')
cursor = conn.cursor()

# Insert artists
cursor.execute("INSERT INTO artist (name) VALUES ('Taylor Swift')")
cursor.execute("INSERT INTO artist (name) VALUES ('The Beatles')")

# Insert albums
cursor.execute("INSERT INTO album (name, artist_id) VALUES ('1989', 1)")
cursor.execute("INSERT INTO album (name, artist_id) VALUES ('Abbey Road', 2)")

# Insert songs
cursor.execute("INSERT INTO song (name, album_id, track_number, duration_seconds) VALUES ('Blank Space', 1, 1, 231)")
cursor.execute("INSERT INTO song (name, album_id, track_number, duration_seconds) VALUES ('Style', 1, 2, 215)")
cursor.execute("INSERT INTO song (name, album_id, track_number, duration_seconds) VALUES ('Come Together', 2, 1, 259)")
cursor.execute("INSERT INTO song (name, album_id, track_number, duration_seconds) VALUES ('Something', 2, 2, 182)")

conn.commit()
conn.close()
print("Mock music data inserted.")
