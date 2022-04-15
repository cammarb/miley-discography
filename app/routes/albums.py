from flask import Flask, redirect, url_for, render_template
from flask import Blueprint
from app.models.album import Album

blueprint = Blueprint("albums", __name__)


@blueprint.get("/")
def get_albums():
    return render_template("list_albums.html")
