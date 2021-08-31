# Music Time Machine Project
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from decouple import config
from pprint import pprint as pp

SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URL = config('SPOTIFY_REDIRECT_URL')

get_date = input(
    "Which year do you want to travel to? Type the date in this form: YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{get_date}"

top_100_songs_response = requests.get(url)

soup = BeautifulSoup(top_100_songs_response.text, "html.parser")

title_tag_of_top_100 = soup.find_all(
    "span", class_="chart-element__information__song text--truncate color--primary")

title_of_top_100 = [title.text for title in title_tag_of_top_100]

# authenticate with spotify
scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URL, scope=scope))

# get my spotify username
username = sp.current_user()['id']
songs_uri = []

# searches for the uri of the top 100 songs in the hot 100 chart
for song in title_of_top_100:
    result = sp.search(q=song, limit=1, type='track')
    try:
        songs_uri.append(result['tracks']['items'][0]['uri'].split(':')[2])
    except IndexError:
        print("Track not in top 100")

# create a playlist
playlist_name = "YYYY-MM-DD Billboard 100"

spotify_playlist = sp.user_playlist_create(username, playlist_name,
                                           public=False)

spotify_playlist_id = spotify_playlist['id']

# add songs to the playlist
for song in songs_uri:
    sp.user_playlist_add_tracks(
        user=username, playlist_id=spotify_playlist_id, tracks=[song])
