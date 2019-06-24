# -*- coding: utf-8 -*-
"""
@author: Grawl, grawler@gmail.com, https://github.com/Grawler

DeezerArtistCollect/config.py
"""

# Visit Deezer.com with your browser and log in. On the left side will be
# a menu with your music. Find the url, your id will be inside it.
#
# Example: https://www.deezer.com/profile/498247221
#                                         ^^^^^^^^^

deezer_id = "498247221"

# These playlists will be ignored while scanning them. Useful when you
# have some general playlists that aren't part of your main music collection.
# You can find these playlists IDs at the Deezer website, on your profile.
#
# Example: https://www.deezer.com/playlist/5711701342
#                                          ^^^^^^^^^^
#
# NOT IMPLEMENTED YET!!!

ignore_playlist_ids = ["5710929302",
                    "5711701342",
                    "5736222702",
                    "5810011802",
                    "888931541"]