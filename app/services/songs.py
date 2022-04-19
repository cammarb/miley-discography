from app.models.album import Album
from app.models.artist import Artist
from app.models.song import Song


def create_song(req_form):
    new_song = Song(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        album_id=req_form.get("album_id"),
        length=req_form.get("length"),
    )
    new_song.save()
    list_of_artists = req_form.getlist("main_artist")
    for i in range(len(list_of_artists)):
        artist = Artist.query.get(list_of_artists[i])
        new_song.song_artist.append(
            artist
        )  # Add to helper table relationship between Song and Artists
        new_song.save()

    # Everytime you create a song the amount of songs in that album
    # gets updated by searching all created songs related to that album_id
    song_album = Album.query.get(new_song.album_id)
    song_album.number_of_songs = Song.query.filter_by(
        album_id=new_song.album_id
    ).count()
    song_album.save()
