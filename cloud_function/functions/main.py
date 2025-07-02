# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app

# For cost control, you can set the maximum number of containers that can be
# running at the same time. This helps mitigate the impact of unexpected
# traffic spikes by instead downgrading performance. This limit is a per-function
# limit. You can override the limit for each function using the max_instances
# parameter in the decorator, e.g. @https_fn.on_request(max_instances=5).

from pathlib import Path
import json

import faiss
import numpy as np

import sqlite3

set_global_options(max_instances=10)
initialize_app()


# Get the path to the current file (main.py)
current_dir = Path(__file__).parent

# Access files inside the db/ folder
songs_db_path = current_dir / "db" / "songs.db"
songs_vector_db_path = current_dir / "db" / "songs.index"

@https_fn.on_request()
def receive_vector(request: https_fn.Request) -> https_fn.Response:
    if request.method != 'POST':
        return https_fn.Response("Method Not Allowed", status=405)

    try:
        data = request.get_json(force=True)

        # Validate input
        if not isinstance(data, list):
            return https_fn.Response(
                json.dumps({"status": "error", "message": "Expected a JSON array."}),
                status=400,
                headers={"Content-Type": "application/json"}
            )

        # Example processing: count elements
        # Load index from file
        index = faiss.read_index(str(songs_vector_db_path))

        # Query vector (must also be float32 and 2D)
        query = np.array(data, dtype='float32').reshape(1, -1)

        # Search: find top 3 match
        distances, indices = index.search(query, 2)

        closest_match = indices.tolist()[0][-1]
        closest_distance = distances.tolist()[0][-1]

        return https_fn.Response(
            json.dumps({
                "status": "success",
                "vector": data,
                "closest_match_index": closest_match,
                "distance": closest_distance
            }),
            status=200,
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        return https_fn.Response(
            json.dumps({"status": "error", "message": str(e)}),
            status=400,
            headers={"Content-Type": "application/json"}
        )