# constants gathered in one place
import pygame, os

# window
scaling = 1.5
windowWidth = int(scaling * 650)
windowHeight = int(scaling * 400)
fps = 30

# stache
stacheMaxAcceleration = 2
stacheDeceleration = -0.2
stacheMaxSpeed = 20
stacheDirectionChange = 10 # in degrees
stacheStartingLives = 3
stacheFiringInterval = fps * 0.5 # fires twice a second

# bullet
bulletLaunchSpeed = 9 # how fast it travels relative the stache when it is fired
bulletStartingLifetime = int(scaling * fps * 1) # how long it will last for before disappearing

# monocle
monocleMinSize = 22
monocleMaxSize = 110
maxMonocles = 5