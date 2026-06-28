from shazamio import Shazam


async def recognize_song(audio_path: str):

    shazam = Shazam()

    result = await shazam.recognize(audio_path)

    if "track" not in result:
        return None

    track = result["track"]

    return {
        "title": track.get("title"),
        "artist": track.get("subtitle"),
        "album": track.get("sections", [{}])[0].get("metadata", []),
        "cover": track.get("images", {}).get("coverart"),
        "url": track.get("url"),
    }
