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

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Album", 1995, 2)
    album2 = Album(1, "Test Album", 1995, 2)
    assert album1 == album2

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Album", 1995, 2)
    assert str(album) == "* 1 - Test Album"