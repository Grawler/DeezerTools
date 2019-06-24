# DeezerTools

Before I used Deezer, I was using Spotify. On each playlist on Spotify, there's a limit of 10,000 songs. This may seem like a lot, but I personally organize my playlists by the first letter of the artist. So playlist 'A' would have artists like ABBA, A Perfect Circle and AFI. Sometimes this would exceed the limit of 10,000 songs and I would start a second playlist called 'A Pt. II'.

When I switched to Deezer I was confronted by their limit, which is only 2,000 per playlist. I split my playlists (using Soundiiz) and converted them to Deezer. Now a certain letter could start with "letter pt. 1" all the way up to "letter pt. 8".

I think for me this is the best way to organize my songs, but whenever there's a new artist or a new album I'll have to manually check all my playlists to see where that certain artist is stored. It's not a huge deal, but it can become bothersome.

This tool was created for my own convenience, but surely I can't be the only person wishing for this feature. Since I started learning Python and I reached the part of lists and dictionaries I knew I had found the foundation needed to create this tool. I'll add more features either as I go or come back to it later.

Before long I realized I wanted to add more features in the future and not just have this one singular purpose. I've renamed the entire project to DeezerTools.

### Prerequisites

You'll need to install Python 3.x and then install the module "requests", see below.

### Installing

- Download or clone this repo so you end up with DeezerArtistCollect.py and the other files somewhere on your PC
- Install Python 3.x
- Install the request module using pip (python -m pip install requests)
- Set up config.py (optional, but recommended)
- Run the Python file for the tool you want to use

DeezerArtistCollect.py: Collects all artists from your playlists and outputs them as "output_DeezerArtistCollect.txt"

## Built With

* [Python 3.x](https://www.python.org/download/releases/3.0/) - Python
* [Requests: HTTP for Humans](https://2.python-requests.org/en/master/) - Requests module

## Changelog

Changelog:

### 0.1:

- Initial release

### 0.2:
- Output artists dictionary as "output_ DeezerArtistCollect.txt"
- Include playlist ID in output
- Create README
- Moved changelog to README
- Created "config.py" for variables (deezer_id)
- Set up ignored_playlist_ids for later use in config.py
- Renamed project to DeezerTools

## ToDo

- File saving/loading so it doesn't have to cycle through the entire
  playlists collection
- Also report when artist is found in another playlist
- Check if playlist has changed in size, if not ignore
- Ability to ignore certain playlists by id
- Throw exception when a variable is invalid

## Feature Tools

- Check if artist's first letter belongs in playlist
- Check number of songs in playlist and reports back

## License

See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Nikita Kholin for his article about the Deezer API (https://kholinlabs.com/getting-your-releases-from-deezer)
