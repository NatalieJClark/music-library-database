from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        choice = input("What would you like to do?\n 1 - List all albums\n 2 - List all artists\nEnter your choice: ")
        album_repository = AlbumRepository(self._connection)
        artist_repository = ArtistRepository(self._connection)
        if choice == "1":
            print("\nHere is the list of albums:")
            for album in album_repository.all():
                print(album)
        elif choice == "2":
            print("\nHere is the list of artists:")
            for artist in artist_repository.all():
                print(artist)
        else:
            print("Invalid choice")

if __name__ == '__main__':
    app = Application()
    app.run()