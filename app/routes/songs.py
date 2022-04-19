from flask import Flask, jsonify, redirect, request, url_for, render_template
from flask import Blueprint
from app.models.song import Song
from app.models.artist import Artist
from app.models.album import Album
from flask_sqlalchemy import SQLAlchemy
from app.services.main import get_all
from app.services.songs import create_song

dbb = SQLAlchemy()

blueprint = Blueprint("songs", __name__)


@blueprint.get("/songs")
def get_songs():
    songs = get_all(Song)
    return render_template("songs/list_songs.html", songs=songs)


@blueprint.get("/songs/add_song")
def add_song():
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template("songs/add_song.html", albums=albums, artists=artists)


@blueprint.post("/songs/add_song")
def post_song():
    create_song(request.form)
    return {"Song created successfully."}
