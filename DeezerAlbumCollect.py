# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerTools/DeezerAlbumCollect.py

This tool goes through all playlists and reports what albums are found.
"""

from config import *
import re
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

albums = []
album_list = []
artists = {}
dupe_id = []
error_log = []
playlists = []
playlist_count = 0
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
        
# We just need the IDs from playlists that aren't suppose to be ignored  
    
for dict in playlists:
    currentid = str(dict["id"])
    if currentid not in ignore_playlist_ids:
        playlists_ids.append(currentid)

# Cycle through all playlists

for id in playlists_ids:
    playlist_count += 1
    percentage = round(100*playlist_count/len(playlists_ids),2)
    playlists_tracks = []
    
    print("Processing playlist " + str(playlist_count) + " out of " + str(len(playlists_ids)) + " (" + str(percentage) + "%)" )
    
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
            print("Found " + str(len(playlists_tracks)) + " tracks to process for playlist " + playlist_name)
            all_tracks_loaded = True
    
    for count in range(len(playlists_tracks)):
        album_title = playlists_tracks[count]["album"]["title"]
        album_id = playlists_tracks[count]["album"]["id"]
        artist_name = playlists_tracks[count]["artist"]["name"]
        artist_id = playlists_tracks[count]["artist"]["id"]
        
        album_title_scrubbed = ""
        
        if album_title not in albums and str(artist_id) not in ignore_artist_ids and str(album_id) not in ignore_album_ids:
            albums.append(album_title)
            # Remove unneeded things in the title of an album that's within brackets (such as "Deluxe" or "International")
            album_title_scrubbed = re.sub(regex, "", album_title)
            print ("Added " + album_title + ", scrubbed as " + album_title_scrubbed)
            # The ; is used to split the difference between album title and artist, so this makes sure an album title never contains that symbol
            album_title_scrubbed = re.sub(";", "", album_title_scrubbed)
            album_list.append(album_title_scrubbed + ";" + artist_name)
            
# Output artists dictionary as "output_DeezerAlbumCollect.txt" and    
# artists that were found in multiple playlists as 
# "output_DeezerArtistDupeCollect.txt"
#
# It checks if the dictionaries actually have something in them before
# attempting to write a file

if album_list:    
    with open("output_DeezerAlbumCollect.txt", "w+", encoding='utf-8') as f:
        for item in album_list:
            f.write("%s\n" % item)
        
# If an error got caught, output them
        
if error_log:
    with open("output_ErrorLog_DeezerAlbumCollect.txt", "w+", encoding='utf-8') as f:
        print(error_log, file=f)   