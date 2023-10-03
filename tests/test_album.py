from lib.album import Album

"""
Album constructs with id, title, release_year and album_id
"""
def test_album_constructs():
    album = Album(1, "OK Computer", 1997, 3)
    assert album.id == 1
    assert album.title == "OK Computer"
    assert album.release_year == 1997
    assert album.artist_id == 3