from flask import Blueprint, jsonify, render_template, request, url_for

# from app.models.artist import Artist
from app.models.song import Artist

blueprint = Blueprint("artists", __name__)


@blueprint.get("/artist")
def get_artist():
    return render_template("artist/add_artist.html")


@blueprint.post("/artist")
def post_artist():
    new_artist = Artist(name=request.form.get("name"))
    new_artist.save()
    return jsonify({"id": new_artist.id, "name": new_artist.name})


# @blueprint.get("/artist/<int:id>")
# def get_single_artist(id):
#     return render_template("artist/add_artist.html")
