<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerArtistCollect

Collects all artist stored in user's playlists and reports back which
 artist is located in what playlist
 
Thanks to Nikita Kholin for explaining some of the Deezer API:
    https://kholinlabs.com/getting-your-releases-from-deezer
    
To-Do:
    - File saving/loading so it doesn't have to cycle through the entire
      playlists collection
    - Also report when artist is found in another playlist
    - Ability to ignore certain playlists by id
    - Check if playlist has changed in size, if not ignore
    - Check if artist's first letter belongs in playlist
    - Make deezer_id a parameter instead of having to set it up in this
      file
    - Output artists dictionary
    
Changelog:
    - 0.1: Initial release
"""

import requests

# Change to your own deezer_id (open a browser, point it to Deezer,
# click on a menu item on the left)

deezer_id = "498247221"

artists = {}
playlists = []
playlists_ids = []

# Set up first run

all_playlists_loaded = False
url = f"https://api.deezer.com/user/" + deezer_id + "/playlists"

# Collect all the playlists from deezer_id, if there is no "next" entry,
# all is loaded

while not all_playlists_loaded:
    r = requests.get(url).json()
    playlists += r['data']
    if r.get('next'):
        url = r['next']
    else:
        all_playlists_loaded = True
        
# We just need the IDs    
    
for dict in playlists:
    playlists_ids.append(dict['id'])

# Cycle through all playlists

for id in playlists_ids:
    url = f"https://api.deezer.com/playlist/" + str(id)
    r = requests.get(url).json()
    playlist_name = r['title']
    number_of_tracks = len(r['tracks']['data'])
    
    for count in range(number_of_tracks):
        artist_name = r['tracks']['data'][count]['artist']['name']
        if artist_name not in artists:
            artists[artist_name] = playlist_name
            print ("Added " + artist_name + ", found in " + playlist_name)

# (Optional) Print artists dictionary

=======
# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerArtistCollect

Collects all artist stored in user's playlists and reports back which
 artist is located in what playlist
 
Thanks to Nikita Kholin for explaining some of the Deezer API:
    https://kholinlabs.com/getting-your-releases-from-deezer
    
To-Do:
    - File saving/loading so it doesn't have to cycle through the entire
      playlists collection
    - Also report when artist is found in another playlist
    - Ability to ignore certain playlists by id
    - Check if playlist has changed in size, if not ignore
    - Check if artist's first letter belongs in playlist
    - Make deezer_id a parameter instead of having to set it up in this
      file
    - Output artists dictionary
    
Changelog:
    - 0.1: Initial release
"""

import requests

# Change to your own deezer_id (open a browser, point it to Deezer,
# click on a menu item on the left)

deezer_id = "498247221"

artists = {}
playlists = []
playlists_ids = []

# Set up first run

all_playlists_loaded = False
url = f"https://api.deezer.com/user/" + deezer_id + "/playlists"

# Collect all the playlists from deezer_id, if there is no "next" entry,
# all is loaded

while not all_playlists_loaded:
    r = requests.get(url).json()
    playlists += r['data']
    if r.get('next'):
        url = r['next']
    else:
        all_playlists_loaded = True
        
# We just need the IDs    
    
for dict in playlists:
    playlists_ids.append(dict['id'])

# Cycle through all playlists

for id in playlists_ids:
    url = f"https://api.deezer.com/playlist/" + str(id)
    r = requests.get(url).json()
    playlist_name = r['title']
    number_of_tracks = len(r['tracks']['data'])
    
    for count in range(number_of_tracks):
        artist_name = r['tracks']['data'][count]['artist']['name']
        if artist_name not in artists:
            artists[artist_name] = playlist_name
            print ("Added " + artist_name + ", found in " + playlist_name)

# (Optional) Print artists dictionary

>>>>>>> e7ab9e55ea3139d0747a5ce0df6913947b701945
# print (artists)