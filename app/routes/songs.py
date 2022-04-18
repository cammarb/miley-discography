from flask import Flask, jsonify, redirect, request, url_for, render_template
from flask import Blueprint
from app.models.song import Song
from app.models.artist import Artist
from app.models.album import Album
from flask_sqlalchemy import SQLAlchemy

dbb = SQLAlchemy()

blueprint = Blueprint("songs", __name__)


@blueprint.get("/songs")
def get_songs():
    return render_template("songs/list_songs.html")


@blueprint.get("/songs/add_song")
def add_song():
    albums = Album.query.all()
    artists = Artist.query.all()
    return render_template("songs/add_song.html", albums=albums, artists=artists)


@blueprint.post("/songs/add_song")
def post_song():
    new_song = Song(
        title=request.form.get("title"),
        slug=request.form.get("slug"),
        album_id=request.form.get("album_id"),
        length=request.form.get("length"),
    )
    new_song.save()
    list_of_artists = request.form.getlist("main_artist")
    for i in range(len(list_of_artists)):
        artist = Artist.query.get(list_of_artists[i])
        new_song.song_artist.append(artist)
        new_song.save()

    song_album = Album.query.get(new_song.album_id)
    song_album.number_of_songs = Song.query.filter_by(
        album_id=new_song.album_id
    ).count()
    song_album.save()
    return jsonify(
        {
            "id": new_song.id,
            "title": new_song.title,
            "slug": new_song.slug,
            "length": new_song.length,
            "album_id": new_song.album_id,
        }
    )
