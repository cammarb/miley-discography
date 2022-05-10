from app.models.artist import Artist


def create_artist(req_form):
    new_artist = Artist(name=req_form.get("name"))
    new_artist.save()


def update_artist(req_form, id):
    artist = Artist.query.get(id)
    artist.name = req_form.get("name")
    artist.save()


def delete(id):
    artist = Artist.query.get(id)
    artist.delete()
