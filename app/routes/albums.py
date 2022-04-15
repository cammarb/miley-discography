from flask import Flask, redirect, url_for, render_template
from flask import Blueprint
from app.models.album import Album

blueprint = Blueprint("albums", __name__)


@blueprint.get("/albums")
def get_albums():
    albums = Album.query.all()
    return render_template("albums/list_albums.html", albums=albums)


# @blueprint.get("/albums")
# def get_album():
#     albums = Album.query.all()
#     return render_template("albums/list_albums.html", albums=albums)


# @blueprint.get("/albums/<int:id>")
# def get_album(id):
#     album = Album.query.get(id)
#     return render_template("albums/.html", album=album)


# @blueprint.post('/albums')
# def add_album():
