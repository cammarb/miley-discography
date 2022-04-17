from flask import Flask, jsonify, redirect, request, url_for, render_template
from flask import Blueprint
from datetime import datetime
from app.models.album import Album
from app.models.artist import Artist

blueprint = Blueprint("albums", __name__)


@blueprint.get("/albums")
def get_albums():
    albums = Album.query.all()
    return render_template("albums/list_albums.html", albums=albums)


@blueprint.get("/albums/add_album")
def get_album():
    artists = Artist.query.all()
    return render_template("albums/add_album.html", artists=artists)


@blueprint.post("/albums/add_album")
def post_album():
    new_album = Album(
        title=request.form.get("title"),
        slug=request.form.get("slug"),
        release_date=datetime.strptime(request.form.get("release_date"), "%Y-%m-%d"),
        is_live=request.form.get("is_live"),
        is_ep=request.form.get("is_ep"),
        number_of_songs=0,
        total_length=request.form.get("total_length"),
        artist_id=request.form.get("artist_id"),
    )
    new_album.save()
    return jsonify(
        {
            "id": new_album.id,
            "title": new_album.title,
            "slug": new_album.slug,
            "release_date": new_album.release_date,
            "is_live": new_album.is_live,
            "is_ep": new_album.is_ep,
            "total_length": new_album.total_length,
            "artist_id": new_album.artist_id,
        }
    )


# @blueprint.get("/albums/<int:id>")
# def get_album(id):
#     album = Album.query.get(id)
#     return render_template("albums/.html", album=album)


# @blueprint.post('/albums')
# def add_album():
