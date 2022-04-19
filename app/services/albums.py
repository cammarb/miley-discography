from app.models.album import Album
from datetime import datetime


def create_album(req_form):
    new_album = Album(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        release_date=datetime.strptime(req_form.get("release_date"), "%Y-%m-%d"),
        is_live=req_form.get("is_live"),
        is_ep=req_form.get("is_ep"),
        number_of_songs=0,
        total_length=req_form.get("total_length"),
        artist_id=req_form.get("artist_id"),
    )
    new_album.save()
