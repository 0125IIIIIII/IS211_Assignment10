import sqlite3

conn = sqlite3.connect('music.db')
cursor = conn.cursor()

# Join query to show songs with album and artist
cursor.execute('''
SELECT song.name, song.track_number, song.duration_seconds, album.name, artist.name
FROM song
JOIN album ON song.album_id = album.id
JOIN artist ON album.artist_id = artist.id
''')

for row in cursor.fetchall():
    song_name, track, duration, album_name, artist_name = row
    print(f"{artist_name} - {album_name} - Track {track}: {song_name} ({duration} sec)")

conn.close()

