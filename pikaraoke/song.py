# Author: Matthew Bowden, Nate Kaldor
import taglib

class Song(object):

    #God I hope this is correct
    def __init__(self, mp3_path = "", artist = "", title = ""):
        """
        Load in mp3 tag data given mp3 path
        :param mp3_path: Path to mp3 file
        :param cdg_path: Path to cdg file
        """
        self._song = taglib.File(mp3_path)
        self._title = title
        self._artist = artist

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, mp3_path):
        self._song = taglib.File(mp3_path)

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, mp3_path):
        song = taglib.File(mp3_path)
        self._artist = song.tags['ARTIST']

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, mp3_path):
        song = taglib.File(mp3_path)
        self._title = song.tags['TITLE']