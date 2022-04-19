from gzip import READ
from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from app.models.artist import Artist
from app.services.main import get_all, get_one
from app.services.artists import create_artist

blueprint = Blueprint("artists", __name__)


@blueprint.get("/artists")
def get_artists():
    artists = get_all(Artist)
    return render_template("artists/list_artists.html", artists=artists)


# Delete artist from table
@blueprint.post("/artists")
def delete_artist():
    artist = get_one(Artist, request.form.get("artist_id"))
    artist.delete()
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
