from gzip import READ
from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from app.models.artist import Artist
from app.models.album import Album
from app.models.song import SongArtist, SongFeaturing
from app.services.main import get_all, get_one
from app.services.artists import create_artist, edit_artist, delete

blueprint = Blueprint("artists", __name__)


@blueprint.get("/artists")
def get_artists():
    artists = get_all(Artist)
    return render_template("artists/list_artists.html", artists=artists)


# Add artist
@blueprint.get("/artists/add")
def add_artist():
    return render_template("artists/add_artist.html")


@blueprint.post("/artists/add")
def post_artist():
    create_artist(request.form)
    return redirect(url_for("artists.get_artists"))


# Edit artist
@blueprint.get("/artists/<int:id>")
def get_artist(id):
    artist = get_one(Artist, id)
    artist_albums = Album.query.filter_by(artist_id=id).count()
    artist_songs = SongArtist.query.filter_by(artist_id=id).count()
    featuring_songs = SongFeaturing.query.filter_by(featuring_id=id).count()
    return render_template(
        "artists/artist.html",
        artist=artist,
        artist_songs=artist_songs,
        featuring_songs=featuring_songs,
        artist_albums=artist_albums,
    )


@blueprint.post("/artists/<int:id>/update")
def update_artist(id):
    edit_artist(request.form, id)
    return redirect(url_for("artists.get_artists"))


# Delete artist
@blueprint.post("/artists/<int:id>/delete")
def delete_artist(id):
    delete(id)
    return redirect(url_for("artists.get_artists"))
