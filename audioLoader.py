#Loads audio files
#For the game ClassyStache
#Writen by Taylor Poulos
#October 2012

import pygame, os
import settingsloader as s

#Because of the streaming nature of the music player, the music is represented by a path
startMusic = os.path.join('sound', 'startMusic.ogg')
gameMusic = os.path.join('sound', 'gameMusic.ogg')
endMusic = os.path.join('sound', 'endMusic.ogg')

#These sound effects are lists because eventually there will be multiple source files
#So that the sound does not get monotonous 
fire = [os.path.join('sound', 'fire.ogg')]
glass = [os.path.join('sound', 'glass.ogg')]
damage = [os.path.join('sound', 'damage0.ogg'), 
          os.path.join('sound', 'damage1.ogg'), 
          os.path.join('sound', 'damage2.ogg')]
