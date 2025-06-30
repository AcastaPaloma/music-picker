import numpy as np
import faiss

import pandas as pd
from pathlib import Path
import os

import sqlite3

sql_file = "song_name_to_id.db"

if os.path.exists(sql_file):
    os.remove(sql_file)
    print(f"Removed existing database file: {sql_file}")

dimension = 8

df = pd.read_csv(Path(os.path.dirname(os.path.abspath(__file__))) / "tracks_features.csv")

selected_headers_song_name = df["name"].tolist()

selected_headers_array = df[["valence", "tempo", "speechiness", "loudness", "instrumentalness", "energy", "danceability", "acousticness"]].to_numpy()

vectors = np.array(selected_headers_array, dtype="float32")
index = faiss.IndexFlatL2(dimension)
index.add(vectors)
faiss.write_index(index, "songs.index")


db_file = "songs.db"
conn = sqlite3.connect("songs.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, song_name TEXT)")
cursor.executemany("INSERT INTO songs (id, song_name) VALUES (?, ?)", 
                   [(i+1, song) for i, song in enumerate(selected_headers_song_name)])
conn.commit()
