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




# Not sure how to translate this to the class yet, but it works in Xubuntu...hopefully that means it works in Raspbian.

# Create a VLC Instance; Everything else flows from the Instance.
instance = vlc.Instance()

# Create a MediaPlayer with the default instance
player = instance.media_player_new()

# Load the media file
media = instance.media_new('/home/nathaniel/Desktop/2 Pac - California Love [SF Karaoke].mp3')

# not sure this line is necessary
# media.get_mrl()

# Add the media to the player
player.set_media(media)

# Subtitles open full screen
player.set_fullscreen(True)

# These are the four states that dictate it's playing
# 1 = Opening
# 2 = Buffering
# 3 = Playing
# 4 = Paused
playing = set([1, 2, 3, 4])
player.play()

# This gives it enough time to get the length of the song and start playing
time.sleep(1)
duration = player.get_length()/1000
mm, ss = divmod(duration, 60)
print("Length:", "%02d:%02d" % (mm,ss))

# Code runs until the song stops
while True:
    state = player.get_state()
    if state not in playing:
        break
    continue

