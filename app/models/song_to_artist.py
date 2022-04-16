from app.extensions.database import db, CRUD_mixing


class SongToArtist(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)
    order = db.Column(db.Integer)
