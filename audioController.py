#Handles audio control
#For the game ClassyStache
#Writen by Taylor Poulos
#October 2012

import sprites
import settingsloader as s
import bigimageloader as img
import gui as u
import audioLoader as audio

def playStartMusic(mixer):
    mixer.music.load(audio.startMusic)
    mixer.music.set_volume(0.3)
    mixer.music.play()

def playGameMusic(mixer):
    mixer.music.load(audio.gameMusic)
    mixer.music.play()
    
def playEndMusic(mixer):
    mixer.music.load(audio.endMusic)
    mixer.music.play()

def fire(mixer):
    play(mixer, audio.fire[0], volume = 0.3)
    
def glass(mixer):
    play(mixer, audio.glass[0], volume = 0.5)
    
def damage(mixer, lives):
    if(lives>1):
        play(mixer, audio.damage[2], volume = 0.7)
    elif(lives==1):
        play(mixer, audio.damage[1], volume = 0.9)
    elif(lives==0):
        play(mixer, audio.damage[0], volume = 0.7)
    
def play(mixer, filepath, volume = 0.5):
    sound = mixer.Sound(filepath)
    sound.set_volume(volume)
    sound.play()