from flask import redirect, request, render_template, url_for
from flask import Blueprint
from app.models.song import Song, SongArtist, SongFeaturing
from app.models.artist import Artist
from app.models.album import Album
from flask_sqlalchemy import SQLAlchemy
from app.services.main import get_all, get_one
from app.services.songs import create_song, edit_song, delete

dbb = SQLAlchemy()

blueprint = Blueprint("songs", __name__)


@blueprint.get("/songs")
def get_songs():
    songs = get_all(Song)
    return render_template("songs/list_songs.html", songs=songs)


@blueprint.get("/songs/<int:id>")
def get_song(id):
    song = get_one(Song, id)
    song_artists = get_all(SongArtist)
    song_featurings = get_all(SongFeaturing)
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template(
        "songs/song.html",
        song=song,
        albums=albums,
        artists=artists,
        song_artists=song_artists,
        song_featurings=song_featurings,
    )


@blueprint.post("/songs/<int:id>/edit")
def update_song(id):
    edit_song(request.form, id)
    return redirect(url_for("songs.get_songs"))


@blueprint.post("/songs/<int:id>/delete")
def delete_song(id):
    delete(id)
    return redirect(url_for("songs.get_songs"))


@blueprint.get("/songs/add_song")
def add_song():
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template("songs/add_song.html", albums=albums, artists=artists)


@blueprint.post("/songs/add_song")
def post_song():
    create_song(request.form)
    return "Song created successfully."
