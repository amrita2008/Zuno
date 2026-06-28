from pathlib import Path

from shazamio import Shazam


async def recognize_song(audio_path):

    shazam = Shazam()

    result = await shazam.recognize(audio_path)

    return result
