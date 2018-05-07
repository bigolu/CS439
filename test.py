import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

songs = []

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        songs.append(item)
        track = item['track']
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')

p = None

while playlists:
    for i, playlist in enumerate(playlists['items']):
        name = playlist['name']
        if 'United States' in name:
            p = playlist
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


results = sp.user_playlist('spotifycharts', p['id'], fields="tracks,next")
tracks = results['tracks']
show_tracks(tracks)
while tracks['next']:
    tracks = sp.next(tracks)
    show_tracks(tracks)


songs2 = sp.audio_features(tracks=[s['track']['uri'] for s in songs])

# make csv
rows = ['{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(s['id'], songs[i]['track']['name'], songs[i]['track']['artists'][0]['name'], s['danceability'], s['energy'], s['key'], s['loudness'], s['mode'], s['speechiness'], s['acousticness'], s['instrumentalness'], s['liveness'], s['valence'], s['tempo'], s['duration_ms'], s['time_signature']) for i, s in enumerate(songs2)]

csv_string = '\n'.join(rows)

print(csv_string)
