# handles gui stuff

import pygame, sys
from pygame.locals import *
import settingsloader as s
import bigimageloader as img

def drawScore(display, score):
	if score == 0:
		img.digitImageRects[0].top = 0
		img.digitImageRects[0].right = s.windowWidth
		display.blit(img.digitImages[0], img.digitImageRects[0])
	i = 0
	while score > 0:
		img.digitImageRects[int(score % 10)].top = 0
		img.digitImageRects[int(score % 10)].right = s.windowWidth-(30 * i)
		display.blit(img.digitImages[int(score % 10)], img.digitImageRects[int(score % 10)])
		score /= 10
		i += 1

def drawLives(display, lives):
	display.blit(img.livesImages[lives-1], img.livesImageRects[lives-1])

def drawLevel(display, level):
	img.levelRect.bottom = s.windowHeight
	display.blit(img.levelImage, img.levelRect)

	tens = level // 10
	ones = level % 10
	
	img.digitImageRects[tens].bottom = img.levelRect.bottom
	img.digitImageRects[tens].left = img.levelRect.width + 10

	img.digitImageRects[ones].bottom = img.levelRect.bottom
	img.digitImageRects[ones].left = img.levelRect.width + img.digitImageRects[tens].width + 10
	
	display.blit(img.digitImages[tens], img.digitImageRects[tens])
	display.blit(img.digitImages[ones], img.digitImageRects[ones])
	
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