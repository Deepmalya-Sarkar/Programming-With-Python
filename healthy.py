from pygame import mixer
import time


while True:
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play()

    p=input("Enter exdone if over\n")
    if p=="exdone": 
        mixer.music.stop()
    time.sleep(6)
    continue
