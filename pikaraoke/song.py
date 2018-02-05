# Author: Matthew Bowden, Nate Kaldor
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Shortcut to see what EasyID3 allows you to get from the audio file
# This may be useful in future developments
# print(EasyID3.valid_keys.keys())

class Song(object):

    def __init__(self, mp3_path, cdg_path):
        """
        Load in mp3 tag data given mp3 path
        :param mp3_path: Path to mp3 file
        :param cdg_path: Path to cdg file
        """
        self._mp3_path = mp3_path
        self._cdg_path = cdg_path
        self._song = MP3(mp3_path, ID3 = EasyID3)
        
        # Make sure that the song file has a matching lyrics file
        # assert self._cdg_path == self._mp3_path.replace('.mp3', '.cdg')

    @property
    def artist(self):
        return self._song['artist']

    @property
    def title(self):
        return self._song['title']

    #This didn't work
    @property
    def length(self):
        return self._song.info.length

# debug statements
test_song = Song("/Users/nate/Desktop/2 Pac - California Love [SF Karaoke].mp3", None)
print("Artist:", test_song.artist, "Title:", test_song.title, "Length:", test_song.length)

song = MP3("/Users/nate/Desktop/2 Pac - California Love [SF Karaoke].mp3", ID3 = EasyID3)
# print(song.pprint())