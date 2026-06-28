import asyncio
from utils.song_recognition import recognize_song
import streamlit as st
from pathlib import Path


def show_home():

    st.image("assets/banner.png", use_container_width=True)

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "flac", "ogg"],
    )

    if uploaded_file:

        st.success(f"Uploaded: {uploaded_file.name}")

        if st.button("Recognize Song"):

            with st.spinner("Recognizing song..."):

    result = asyncio.run(
        recognize_song(uploaded_file)
    )

if result is None:

    st.error("Song not recognized.")

else:

    st.success("Song recognized!")

    st.image(result["cover"], width=250)

    st.subheader(result["title"])

    st.write(f"Artist : {result['artist']}")

    st.write(result["url"])
    st.markdown("---")

    st.subheader("Recent Songs")

    st.dataframe(
        {
            "Song": [],
            "Artist": [],
            "Language": [],
            "Mood": [],
        },
        use_container_width=True,
        hide_index=True,
    )
