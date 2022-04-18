from app.extensions.database import db, CRUD_mixing


class Song(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    song_to_artist = db.relationship("SongToArtist", backref="song", lazy=True)
    song_to_featuring = db.relationship("SongToFeaturing", backref="song", lazy=True)
    length = db.Column(db.String, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"))
    album = db.relationship("Album", back_populates="tracklist")
