from app.models.artist import Artist


def create_artist(req_form):
    new_artist = Artist(name=req_form.get("name"))
    new_artist.save()
