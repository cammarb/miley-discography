from flask import Flask, redirect, url_for, render_template
from flask import Blueprint
from app.models.song import Song

blueprint = Blueprint("songs", __name__)


@blueprint.get("/songs")
def get_songs():
    return render_template("songs/list_songs.html")
