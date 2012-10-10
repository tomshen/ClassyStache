# handles ui stuff

import pygame, sys
from pygame.locals import *
import settingsloader as s
import imageloader as img

def drawScore(display, score):
	if score == 0:
		img.scoreImageRects[0].right = s.windowWidth
		display.blit(img.scoreImages[0], img.scoreImageRects[0])
	i = 0
	while score > 0:
		img.scoreImageRects[score % 10].right = s.windowWidth-(30 * i)
		display.blit(img.scoreImages[score % 10], img.scoreImageRects[score % 10])
		score /= 10
		i += 1

def drawLives(display, lives):
	display.blit(img.livesImages[lives-1], img.livesImageRects[lives-1])
	
def drawScreen(display, screenName):
	display.blit(img.screenImages[screenName], img.screenRects[screenName])
	pygame.display.update()

def drawBackground(display):
	display.blit(img.screenImages['background'], img.screenRects['background'])
	
def showAndWait(display, screenName):
# draws the screen and waits for the user to either press SPACE to continue or ESC to exit
	drawScreen(display, screenName)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				elif event.key == K_SPACE:
					return

def pauseGame(display):
	paused = True
	drawScreen(display, 'pause')
	while paused:
		for event in pygame.event.get():
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					terminate()
				if event.key == event.key == ord('p'):
					paused = False
	drawScreen(display, 'background')
	
def terminate():
    pygame.quit()
    sys.exit()