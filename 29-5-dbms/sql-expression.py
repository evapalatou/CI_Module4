from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey,
    Integer, String, MetaData, select
)

# connect to local chinook database
db = create_engine("postgresql:///chinook")

# SQLAlchemy 2.x style metadata (NO engine passed here)
meta = MetaData()

# -------------------------
# Artist table
# -------------------------
artist_table = Table(
    "Artist",
    meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# -------------------------
# Album table
# -------------------------
album_table = Table(
    "Album",
    meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# -------------------------
# Track table
# -------------------------
track_table = Table(
    "Track",
    meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# -------------------------
# Queries
# -------------------------
with db.connect() as connection:

     # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(artist_table.c.Name)

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 (active one): tracks where composer = 'Queen'
    # select_query = select(track_table).where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)

    for row in results:
        print(row)