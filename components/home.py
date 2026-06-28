import streamlit as st


def show_home():

    st.title("ZUNO")
    st.caption("AI Music Intelligence Platform")

    st.divider()

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown("## Discover. Understand. Personalize.")

        st.write(
            """
            Zuno is an AI-powered music intelligence platform that identifies
            songs, translates lyrics into multiple languages, analyzes listener
            emotions, generates personalized recommendations, and creates
            intelligent playlists.
            """
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Languages", "50+")
            st.metric("Recommendation Engine", "Enabled")

        with col2:
            st.metric("AI Modules", "5")
            st.metric("Real-time Analysis", "Available")

    with right:

        st.image(
            "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=900",
            use_container_width=True,
        )

    st.divider()

    st.markdown("## Core Capabilities")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
### Song Recognition

Identify songs from uploaded audio with confidence scoring and metadata.
"""
        )

        st.info(
            """
### Emotion Analysis

Understand the emotional characteristics of music using deep learning.
"""
        )

    with col2:
        st.info(
            """
### Lyrics Translation

Translate lyrics into multiple languages while preserving context.
"""
        )

        st.info(
            """
### Playlist Generation

Create intelligent playlists based on listening preferences.
"""
        )

    with col3:
        st.info(
            """
### AI Recommendations

Generate personalized song recommendations using embeddings.
"""
        )

        st.info(
            """
### Analytics Dashboard

Visualize listening history, genres, artists, and mood trends.
"""
        )

    st.divider()

    st.markdown("## Try Zuno")

    uploaded_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "flac", "ogg"],
    )

    if uploaded_file:

        st.success(f"File received: {uploaded_file.name}")

        st.write("Processing pipeline will be integrated in the next phase.")

    st.divider()

    st.caption("Zuno • AI Music Intelligence Platform")
