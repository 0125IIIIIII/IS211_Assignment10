import unittest
import sqlite3
import os

DB_NAME = 'test_music.db'

class TestMusicSchema(unittest.TestCase):

    def setUp(self):
        # Create a fresh test database
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_schema()
        self.insert_mock_data()

    def tearDown(self):
        self.conn.close()
        os.remove(DB_NAME)

    def create_schema(self):
        self.cursor.executescript('''
        CREATE TABLE artist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE album (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            artist_id INTEGER NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES artist(id)
        );

        CREATE TABLE song (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            album_id INTEGER NOT NULL,
            track_number INTEGER NOT NULL,
            duration_seconds INTEGER NOT NULL,
            FOREIGN KEY (album_id) REFERENCES album(id)
        );
        ''')

    def insert_mock_data(self):
        self.cursor.execute("INSERT INTO artist (name) VALUES ('Taylor Swift')")
        self.cursor.execute("INSERT INTO artist (name) VALUES ('The Beatles')")

        self.cursor.execute("INSERT INTO album (name, artist_id) VALUES ('1989', 1)")
        self.cursor.execute("INSERT INTO album (name, artist_id) VALUES ('Abbey Road', 2)")

        songs = [
            ('Blank Space', 1, 1, 231),
            ('Style', 1, 2, 215),
            ('Come Together', 2, 1, 259),
            ('Something', 2, 2, 182)
        ]
        self.cursor.executemany("INSERT INTO song (name, album_id, track_number, duration_seconds) VALUES (?, ?, ?, ?)", songs)
        self.conn.commit()

    def test_artist_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM artist")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_album_artist_relationship(self):
        self.cursor.execute("SELECT album.name, artist.name FROM album JOIN artist ON album.artist_id = artist.id")
        results = self.cursor.fetchall()
        self.assertIn(('1989', 'Taylor Swift'), results)
        self.assertIn(('Abbey Road', 'The Beatles'), results)

    def test_song_album_relationship(self):
        self.cursor.execute("SELECT song.name, album.name FROM song JOIN album ON song.album_id = album.id")
        results = self.cursor.fetchall()
        self.assertIn(('Blank Space', '1989'), results)
        self.assertIn(('Come Together', 'Abbey Road'), results)

    def test_song_duration(self):
        self.cursor.execute("SELECT name, duration_seconds FROM song WHERE name = 'Something'")
        song = self.cursor.fetchone()
        self.assertEqual(song[1], 182)

if __name__ == '__main__':
    unittest.main()
