from flask import Flask, jsonify, redirect, request, url_for, render_template
from flask import Blueprint
from app.models.album import Album
from app.models.artist import Artist
from app.services.main import get_all, get_one
from app.services.albums import create_album

blueprint = Blueprint("albums", __name__)


# Getting all albums and list them
@blueprint.get("/albums")
def get_albums():
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template("albums/list_albums.html", albums=albums, artists=artists)


# Delete a single album
@blueprint.post("/albums")
def delete_album():
    album = get_one(Album, request.form.get("album_id"))
    album.delete()
    return redirect(url_for("albums.get_albums"))


@blueprint.get("/albums/add_album")
def get_album():
    artists = get_all(Artist)
    return render_template("albums/add_album.html", artists=artists)


@blueprint.post("/albums/add_album")
def post_album():
    create_album(request.form)
    return redirect(url_for("albums.get_albums"))


@blueprint.get("/albums/<string:slug>/edit")
def edit_album(slug):
    return


# @blueprint.get("/albums/<int:id>")
# def get_album(id):
#     album = Album.query.get(id)
#     return render_template("albums/.html", album=album)


# @blueprint.post('/albums')
# def add_album():
