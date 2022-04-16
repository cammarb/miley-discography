from app.extensions.database import db, CRUD_mixing


class Artist(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    albums = db.relationship("Album", backref="artist", lazy=True)
    song_to_artist = db.relationship("SongToArtist", backref="artist", lazy=True)
