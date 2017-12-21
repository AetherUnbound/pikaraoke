# Author: Matthew Bowden, Nate Kaldor
import taglib



class Song(object):

    def __init__(self, mp3_path, cdg_path):
        """
        Load in mp3 tag data given mp3 path
        :param mp3_path: Path to mp3 file
        :param cdg_path: Path to cdg file
        """
        self._mp3_path = mp3_path
        self._cdg_path = cdg_path
        self._song = taglib.File(mp3_path)

        # some assertion that _mp3_path is in the same folder as _cdg_path
        assert self._cdg_path == self._mp3_path.replace('.mp3', '.cdg') #This should work for that

    # No need for setters - we're assuming these will stay constant,
    # i.e. the song info is static and won't change
    @property
    def artist(self):
        return self._song.tags['ARTIST']

    @property
    def title(self):
        return self._song.tags['TITLE']
