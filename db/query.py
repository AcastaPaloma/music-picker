import pandas as pd
import os
from pathlib import Path

import faiss
import numpy as np

# Valence, tempo, speechiness, loudness, instrumentalness, energy, danceability, acousticness
# Mode, duration_ms

# Load index from file
index = faiss.read_index("songs.index")

# Query vector (must also be float32 and 2D)
query = np.array([[0.296, 147.661, 0.0468, -3.469, 0.0000012, 0.735, 0.308, 0.363]], dtype='float32')

# Search: find top 1 match
distances, indices = index.search(query, 3)

print("Closest matches: ", indices)
print("Distances:", distances)