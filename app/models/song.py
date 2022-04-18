from app.extensions.database import db, CRUD_mixing


class SongArtist(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)


class SongFeaturing(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), primary_key=True)
    featuring_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)


class Song(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    song_artist = db.relationship(
        "Artist", secondary="song_artist", backref="song_artist", lazy=True
    )
    # song_featuring = db.relationship(
    #     "SongFeaturing", backref="song_featuring", lazy=True
    # )
    length = db.Column(db.String, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"))
    album = db.relationship("Album", back_populates="tracklist")


class Artist(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # song_artist = db.relationship("SongArtist", backref="song_artist", lazy=True)
    # song_featuring = db.relationship(
    #     "SongFeaturing", backref="song_featuring", lazy=True
    # )
    albums = db.relationship("Album", backref="artist", lazy=True)
