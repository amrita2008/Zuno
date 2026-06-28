import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()


client = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    )
)


def search_song(title, artist):

    query = f"track:{title} artist:{artist}"

    result = client.search(
        q=query,
        type="track",
        limit=1
    )

    items = result["tracks"]["items"]

    if len(items) == 0:
        return None

    track = items[0]

    artist_id = track["artists"][0]["id"]

    artist_info = client.artist(artist_id)

    return {
        "album": track["album"]["name"],
        "release_date": track["album"]["release_date"],
        "popularity": track["popularity"],
        "spotify_url": track["external_urls"]["spotify"],
        "album_cover": track["album"]["images"][0]["url"],
        "genres": artist_info["genres"],
    }
