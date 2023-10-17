from pygame import mixer
import os
import time

mixer.init()

mixer.music.load('race.wav')
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)
while True:
    time.sleep(1)
