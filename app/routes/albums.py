from flask import Flask, redirect, url_for, render_template
from flask import Blueprint
from app.models.album import Album

blueprint = Blueprint("albums", __name__)


@blueprint.get("/albums")
def get_albums():
    return render_template("albums/list_albums.html")
