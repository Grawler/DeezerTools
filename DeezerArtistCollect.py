# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerArtistCollect/DeezerArtistCollect.py
"""

from config import *
import requests

# Change to your own deezer_id (open a browser, point it to Deezer,
# click on a menu item on the left)

print("Enter your deezer_id. If left empty it'll use the default stored in " +
      "config.py")
input_id = input("deezer_id: ")
if not input_id:
    input_id = deezer_id
    
artists = {}
playlists = []
playlists_ids = []

# Set up first run

all_playlists_loaded = False
url = f"https://api.deezer.com/user/" + input_id + "/playlists"

# Collect all the playlists from deezer_id, if there is no "next" entry,
# all is loaded

while not all_playlists_loaded:
    r = requests.get(url).json()
    playlists += r["data"]
    if r.get("next"):
        url = r["next"]
    else:
        all_playlists_loaded = True
        
# We just need the IDs    
    
for dict in playlists:
    playlists_ids.append(dict["id"])

# Cycle through all playlists

for id in playlists_ids:
    url = f"https://api.deezer.com/playlist/" + str(id)
    r = requests.get(url).json()
    playlist_name = r["title"]
    number_of_tracks = len(r["tracks"]["data"])
    
    for count in range(number_of_tracks):
        artist_name = r["tracks"]["data"][count]["artist"]["name"]
        if artist_name not in artists:
            artists[artist_name] = playlist_name
            print ("Added " + artist_name + ", found in " + playlist_name +
                   " (" + str(id) + ")")

# Output artists dictionary as"output_artists.txt"
    
with open("output_artists.txt", "w+") as f:
    print(artists, file=f)