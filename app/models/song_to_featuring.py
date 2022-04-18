from app.extensions.database import db, CRUD_mixing


class SongToFeaturing(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), primary_key=True)
    featuring_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)
