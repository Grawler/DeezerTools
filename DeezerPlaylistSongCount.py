# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerTools/DeezerPlaylistSongCount.py

This tool goes through all your playlists and reports the amount of songs
in it.
"""

from config import *
import requests
import time

print("Enter your deezer_id. If left empty it'll use the default stored in " +
      "config.py")
input_id = input("deezer_id: ")
if not input_id:
    input_id = deezer_id
    print("Using " + deezer_id)
else:
    print("Using " + input_id)

error_log = []    
playlists = []
playlists_ids = []
playlist_tracks = {}

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
        
# We just need the IDs from playlists that aren't suppose to be ignored  
    
for dict in playlists:
    currentid = str(dict["id"])
    if currentid not in ignore_playlist_ids:
        playlists_ids.append(currentid)

# Cycle through all playlists

for id in playlists_ids:
    
    url = f"https://api.deezer.com/playlist/" + str(id)
    try:
        r = requests.get(url, timeout=10).json()
    except requests.exceptions.RequestException as e:
        print (e)
        error_log.append(e)
        time.sleep(60)
    playlist_name = r["title"]
    playlist_nb_tracks = str(r["nb_tracks"])
    playlist_tracks[playlist_name] = playlist_nb_tracks
    print("Found " + playlist_nb_tracks + " tracks in " + playlist_name)
    
if playlist_tracks:
    with open("output_DeezerPlaylistSongCount.txt", "w+", encoding='utf-8') as f:
        print(playlist_tracks, file=f)
        
# If an error got caught, output them
        
if error_log:
    with open("output_ErrorLog_DeezerPlaylistSongCount.txt", "w+", encoding='utf-8') as f:
        print(error_log, file=f)           