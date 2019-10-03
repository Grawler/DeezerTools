# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerTools/config.py
"""

# You can find these IDs at the Deezer web player.
#
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
#
# Example: https://www.deezer.com/us/artist/6861265
#                                           ^^^^^^^
#
# 5080 = Various Artists

ignore_artist_ids = ["5080",
                     "6861265"]

# These albums will be ignored while scanning for them.
#
# Example: https://www.deezer.com/us/album/10099334
#                                          ^^^^^^^^ 

ignore_album_ids = []

# If you want extra characters in album titles gone, leave the regex as
# it is, otherwise replace it with ""

regex = "[\(\[].*?[\)\]]"

# NOT IMPLEMENTED YET
#                     NOT IMPLEMENTED YET
#                                         NOT IMPLEMENTED YET
# ignore_song_ids = []
# ignore_album_ids = []
#
# If you keep getting errors while running this program, you may want to
# slow down the requests, where the number is how many seconds the program
# waits before moving on
#
#
# sleepduration = 0
#
# These playlists will be used to scan what albums exist and where. It will
# not list duplicates separately
#
# collect_album_ids = []