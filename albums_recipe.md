# {{Albums}} Model and Repository Classes Design Recipe

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).


```
Table: albums

Columns:
id | title | release_year | artist_id
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Table name: albums

# Model class
# (in lib/album.py)
class Album


# Repository class
# (in lib/slbum_repository.py)
class AlbumRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: albums

# Model class
# (in lib/album.py)

class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.release_year = 
        self.artist_id = 

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():

    # Selecting all albums
    # No arguments
    def all(self):
        # Executes the SQL query:
        #   SELECT * FROM albums;
        # Returns an array of Album objects.
    def find(self, artist_id):
        # Executes the SQL query:
        #   SELECT * FROM albums WHERE %s, [id]
        # Return the album record for the given id

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# Album

"""
Construct album object
"""

album = Album(1, "OK Computer", 1997, 3)
album.id == 1
album.title == "OK Computer"
album.release_year == 1997
album.artist_id == 3

# AlbumRepository

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
db_connection.seed(seeds/music_library.sql)
repository = AlbumRepository(db_connection)
albums = repository.all()
assert albums == [
    Album(1, 'Doolittle', 1989, 1),
    Album(2, 'Surfer Rosa', 1988, 1),
    Album(3, 'Waterloo', 1974, 2),
    Album(4, 'Super Trouper', 1980, 2),
    Album(5, 'Bossanova', 1990, 1),
    Album(6, 'Lover', 2019, 3),
    Album(7, 'Folklore', 2020, 3),
    Album(8, 'I Put a Spell on You', 1965, 4),
    Album(9, 'Baltimore', 1978, 4),
    Album(10, 'Here Comes the Sun', 1971, 4),
    Album(11, 'Fodder on My Wings', 1982, 4),
    Album(12, 'Ring Ring', 1973, 2)
]

"""
When we call AlbumRepository#find with an id
We get the record with that id
"""
db_connection.seed(seeds/music_library.sql)
repository = AlbumRepository(db_connection)
result = repository.find(2)
result == Album(2, 'Surfer Rosa', 1988, 1)
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
