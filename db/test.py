import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your actual credentials
client_id = "b977fc08cd124db690567b2554d99221"
client_secret = "589746e1b5dc471a94fdfcde684b59bc"

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Search for a song
results = sp.search(q="Blinding Lights The Weeknd", type="track", limit=1)
track = results['tracks']['items'][0]
track_id = track['id']

# Get audio features
features = sp.audio_features(track_id)[0]

# Print selected features
print({
    'valence': features['valence'],
    'tempo': features['tempo'],
    'speechiness': features['speechiness'],
    'loudness': features['loudness'],
    'instrumentalness': features['instrumentalness'],
    'energy': features['energy'],
    'danceability': features['danceability'],
    'acousticness': features['acousticness']
})
