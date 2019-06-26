# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerTools/DeezerArtistCollect.py
"""

from config import *
import requests
import time

# Change to your own deezer_id (open a browser, point it to Deezer,
# click on a menu item on the left)

print("Enter your deezer_id. If left empty it'll use the default stored in " +
      "config.py")
input_id = input("deezer_id: ")
if not input_id:
    input_id = deezer_id
    print("Using " + deezer_id)
else:
    print("Using " + input_id)
    
artists = {}
artists_dupe = {}
playlists = []
playlists_ids = []
dupe_id = []
error_log = []

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
    playlists_tracks = []
    
    url = f"https://api.deezer.com/playlist/" + str(id)
    try:
        r = requests.get(url, timeout=10).json()
    except requests.exceptions.RequestException as e:
        print (e)
        error_log.append(e)
        time.sleep(60)
    playlist_name = r["title"]
    
    all_tracks_loaded = False
    url = f"https://api.deezer.com/playlist/" + str(id) + "/tracks"
    try:
        r = requests.get(url, timeout=10).json()
    except requests.exceptions.RequestException as e:
        print (e)
        error_log.append(e)
        time.sleep(60)
    
    while not all_tracks_loaded:     
        try:
            r = requests.get(url, timeout=10).json()
        except requests.exceptions.RequestException as e:
            print (e)
            error_log.append(e)
            time.sleep(60)
        playlists_tracks += r["data"]
        if r.get("next"):
            url = r["next"]
        else:
            print("Found " + str(len(playlists_tracks)) + " tracks to process for " + playlist_name)
            all_tracks_loaded = True
    
    for count in range(len(playlists_tracks)):
        artist_name = playlists_tracks[count]["artist"]["name"]
        artist_id = playlists_tracks[count]["artist"]["id"]
        if artist_name not in artists and str(artist_id) not in ignore_artist_ids:
            artists[artist_name] = playlist_name
            dupe_id.append(id)
            print ("Added " + artist_name + ", found in " + playlist_name + " (" + str(id) + ")")
        elif artist_name in artists and id not in dupe_id and str(artist_id) not in ignore_artist_ids:
            artists[artist_name] += " + " + playlist_name
            dupe_id.append(id)
            print ("Found " + artist_name + " that already exists in other playlist, " + playlist_name + " (" + str(id) + ") added as dupe playlist")
            artists_dupe[artist_name] = artists[artist_name]
            
# Output artists dictionary as
#  "output_DeezerArtistCollect.txt" and    
# artists that were found in multiple playlists as 
#  "output_DeezerArtistDupeCollect.txt"
#
# It checks if the dictionaries actually have something in them before
# attempting to write a file

if artists:    
    with open("output_DeezerArtistCollect.txt", "w+", encoding='utf-8') as f:
        print(artists, file=f)

if artists_dupe:   
    with open("output_DeezerArtistDupeCollect.txt", "w+", encoding='utf-8') as f:
        print(artists_dupe, file=f)
        
# If an error got caught, log them to "output_ErrorLog.txt"  
        
if error_log:
    with open("output_ErrorLog.txt", "w+", encoding='utf-8') as f:
        print(error_log, file=f)   