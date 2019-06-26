# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerTools/config.py
"""

# Visit Deezer.com with your browser and log in. On the left side will be
# a menu with your music. Find the url, your id will be inside it.
#
# Example: https://www.deezer.com/profile/498247221
#                                         ^^^^^^^^^

deezer_id = "498247221"

# These playlists will be ignored while scanning them.
# You can find these playlist IDs at the Deezer website, on your profile.
#
# Example: https://www.deezer.com/playlist/5711701342
#                                          ^^^^^^^^^^

ignore_playlist_ids = ["5710929302",
                       "5711701342",
                       "5736222702",
                       "5810011802",
                       "5768605562",
                       "5768621602",
                       "888931541"]

# These artists will be ignored while scanning for them.
# You can find these artist IDs at the Deezer website, on your profile or in
# any playlist.
#
# Example: https://www.deezer.com/us/artist/6861265
#                                           ^^^^^^^

ignore_artist_ids = ["6861265",
                     "5080"]

# NOT IMPLEMENTED YET

ignore_song_ids = []
ignore_album_ids = []

# If you keep getting errors while running this program, you may want to
# slow down the requests, where the number is how many seconds the program
# waits before moving on
#
# NOT IMPLEMENTED YET

sleepduration = 0