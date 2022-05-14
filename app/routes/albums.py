from flask import redirect, request, url_for, render_template
from flask import Blueprint
from app.models.album import Album
from app.models.artist import Artist
from app.services.main import get_all, get_one
from app.services.albums import create_album, edit

blueprint = Blueprint("albums", __name__)


# Getting all albums and list them
@blueprint.get("/albums")
def get_albums():
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template("albums/list_albums.html", albums=albums, artists=artists)


@blueprint.get("/albums/add_album")
def new_album():
    artists = get_all(Artist)
    return render_template("albums/add_album.html", artists=artists)


@blueprint.post("/albums/add_album")
def post_album():
    create_album(request.form)
    return redirect(url_for("albums.get_albums"))


@blueprint.get("/albums/<int:id>")
def get_album(id):
    album = get_one(Album, id)
    artists = get_all(Artist)
    return render_template("albums/album.html", album=album, artists=artists)


@blueprint.post("/albums/<int:id>/edit")
def edit_album(id):
    edit(request.form, id)
    return redirect(url_for("albums.get_albums"))


# Delete a single album
@blueprint.post("/albums/<int:id>/delete")
def delete_album(id):
    album = get_one(Album, id)
    album.delete()
    return redirect(url_for("albums.get_albums"))
