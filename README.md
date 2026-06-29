# Zuno

## Overview

Zuno is an AI-powered music intelligence platform designed to analyze music through recommendation systems, semantic embeddings, multilingual lyric translation, and personalized listening insights. The project combines natural language processing, deep learning, semantic search, and data analytics into a unified architecture for intelligent music exploration.

The system is organized as a modular AI pipeline where each component performs an independent task while sharing common datasets, embeddings, and metadata.

---

# System Architecture

```
                           User
                             │
                             ▼
                    Streamlit Interface
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 Recommendation Engine   Translation Engine   Live Music Intelligence
        │                    │                    │
        └──────────────┬─────┴────────────────────┘
                       ▼
                Embedding Layer
                       │
             Sentence Transformers
                       │
                       ▼
                 Music Dataset
                       │
          Feature Engineering Pipeline
                       │
                       ▼
                  Analytics Layer
                       │
                       ▼
                Zuno Wrapped Report
```

---

# Repository Structure

```
Zuno/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── data/
│   ├── zuno_dataset.xls
│   ├── recommended_playlist.xls
│   ├── user_history.xls
│   ├── zuno_wrapped.xls
│   └── translations.json
│
├── models/
│   └── zuno_embeddings.npy
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── Recommendation Engine.ipynb
│   ├── translation_engine.ipynb
│   ├── live_music_intelligence.ipynb
│   └── Zuno Wrapped.ipynb
│
├── components/
│
└── utils/
```

---

# Core Components

## Data Processing

The preprocessing pipeline performs data cleaning, normalization, metadata integration, and feature engineering to construct a unified music dataset suitable for downstream machine learning tasks.

---

## Recommendation Engine

The recommendation engine generates semantic music recommendations using transformer-generated embeddings and cosine similarity. Songs are represented in a dense embedding space constructed from musical metadata, lyrical information, and contextual features.

Primary techniques include:

* Sentence Transformers
* Semantic Embeddings
* Cosine Similarity Search
* Vector-based Recommendation

---

## Translation Engine

The translation module provides multilingual lyric translation while preserving semantic context. It is designed to support multiple languages through large language models and structured translation mappings.

---

## Live Music Intelligence

This module performs contextual analysis on music metadata and user interactions to generate insights related to genres, listening behavior, artist relationships, and recommendation context.

---

## Zuno Wrapped

The analytics engine summarizes listening activity by aggregating historical interactions into interpretable insights such as listening preferences, genre distribution, artist statistics, and personalized summaries.

---

# Machine Learning Pipeline

```
Music Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Sentence Embedding Generation
      │
      ▼
Embedding Storage
      │
      ▼
Similarity Computation
      │
      ▼
Recommendation Generation
      │
      ▼
User Analytics
```

---

# Technology Stack

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* Sentence Transformers
* NumPy
* Pandas

## Natural Language Processing

* Transformers
* Semantic Embeddings
* Cosine Similarity

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Plotly

## Interface

* Streamlit

## Development Environment

* Jupyter Notebook
* Git
* GitHub
* GitHub Codespaces

---

# Project Workflow

```
Data Collection
      │
      ▼
Data Preprocessing
      │
      ▼
Embedding Generation
      │
      ▼
Recommendation Modeling
      │
      ▼
Translation Pipeline
      │
      ▼
Analytics Generation
      │
      ▼
Interactive Interface
```

---

# Future Improvements

* Real-time recommendation updates
* Large Language Model assisted music insights
* Audio feature extraction pipeline
* Vector database integration
* Hybrid recommendation system
* User authentication and profile management
* Cloud deployment
* Personalized recommendation fine-tuning
* Distributed embedding retrieval
* Model optimization for large-scale music collections

---

# License

This project is intended for educational, research, and portfolio purposes.

