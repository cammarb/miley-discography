from sqlalchemy import ForeignKey
from app.extensions.database import db, CRUD_mixing


class Song(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    artist = db.Column(db.String, nullable=False)
    featuring = db.Column(db.String)
    lenght = db.Column(db.Time)
    album_id = db.Column(db.Integer, ForeignKey("album.id"))
    album = db.relationship("Album", back_populates="tracklist")
