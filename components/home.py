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

            st.info("Recognition model will run here.")

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
