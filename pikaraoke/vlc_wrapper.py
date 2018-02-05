import vlc
import os
import sys
import time

class vlc_wrapper(object):

    def __init__(self, song, next_song):
        self._current_song = song
        self._next_song_in_queue = next_song
        self._instance = vlc.instance()
        self._player = self._instance.media_player_new()
        self._media = instance.media_new(self._current_song)
        self._playing = set([1,2,3,4])



instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
media = instance.media_new('/Users/nate/Desktop/2 Pac - California Love [SF Karaoke].mp3')
media.get_mrl()
#Add the media to the player
player.set_media(media)

playing = set([1, 2, 3, 4])
player.play()
time.sleep(1)
duration = player.get_length()/1000
mm, ss = divmod(duration, 60)
print("Length:", "%02d:%02d" % (mm,ss))
while True:
    state = player.get_state()
    if state not in playing:
        break
    continue

