from gzip import READ
from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from app.models.artist import Artist
from app.services.main import get_all, get_one
from app.services.artists import create_artist, update_artist, delete

blueprint = Blueprint("artists", __name__)


@blueprint.get("/artists")
def get_artists():
    artists = get_all(Artist)
    return render_template("artists/list_artists.html", artists=artists)


# Edit artist
@blueprint.get("/artists/<int:id>")
def get_artist(id):
    artist = get_one(Artist, id)
    return render_template("artists/artist.html", artist=artist)


@blueprint.post("/artists/<int:id>")
def edit_artist(id):
    update_artist(request.form, id)
    return redirect(url_for("artists.get_artists"))


# Delete artist
@blueprint.post("/artists/<int:id>")
def delete_artist(id):
    artist.delete(id)
    return redirect(url_for("artists.get_artists"))


# Add artist
@blueprint.get("/artists/add")
def add_artist():
    return render_template("artists/add_artist.html")


@blueprint.post("/artists/add")
def post_artist():
    create_artist(request.form)
    return redirect(url_for("artists.get_artists"))


# @blueprint.get("/artist/<int:id>")
# def get_single_artist(id):
#     return render_template("artist/add_artist.html")
