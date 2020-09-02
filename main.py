import pygame, random, os
from pygame.locals import *
#import pygame._view

import sprites
import settingsloader as s
import bigimageloader as img
import gui as u
import audioLoader as audio
import audioController as a

def addMoreMonocles(monocles):
	for i in range(s.maxMonocles):
		monocles.add(sprites.Monocle(random.randint(s.monocleMinSize, s.monocleMaxSize),
						  (random.randint(0, s.windowWidth),
						   random.randint(0, s.windowHeight))))
	
# start and set up display
pygame.init()
pygame.mixer.init()
mixer = pygame.mixer
pygame.display.set_icon(img.iconImage)
mainClock = pygame.time.Clock()
display = pygame.display.set_mode((s.windowWidth, s.windowHeight))
pygame.display.set_caption('ClassyStache')
pygame.mouse.set_visible(False)


#start audio
a.playStartMusic(mixer)

# show the Title display
u.showAndWait(display, 'title')
u.showAndWait(display, 'instruct')
a.playGameMusic(mixer)#Game begins
while True:
	# set up the start of the game
	u.drawBackground(display)
	score = 0
	level = 1
	
	stache = sprites.Stache()
	player = pygame.sprite.Group()
	player.add(stache)
	directionToTurn = 0
	thrustersOn = False
	isFiring = False

	bullets = pygame.sprite.Group()

	monocles = pygame.sprite.Group()
	
	addMoreMonocles(monocles)

	gameOver = False

	while not gameOver: # runs while actually playing the game
		u.drawBackground(display)
		paused = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				u.terminate()

			if event.type == KEYDOWN:
				if event.key == K_UP or event.key == ord('w'):
					thrustersOn = True
				if event.key == K_LEFT or event.key == ord('a'):
					directionToTurn = -1
				if event.key == K_RIGHT or event.key == ord('d'):
					directionToTurn = 1
				if event.key == K_SPACE:
					isFiring = True
					a.fire(mixer)
					bullets.add(stache.fire())
				 
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					u.terminate()
				if event.key == event.key == ord('p'):
					paused = True
				if event.key == K_UP or event.key == ord('w'):
					thrustersOn = False
				if event.key == K_LEFT or event.key == ord('a'):
					directionToTurn = 0
				if event.key == K_RIGHT or event.key == ord('d'):
					directionToTurn = 0
				if event.key == K_SPACE:
					isFiring = False

		# update sprites
		stache.update(display, thrustersOn, directionToTurn, isFiring, bullets)
		bullets.update()
		monocles.update()
		player.clear(display, img.screenImages['background'])
		bullets.clear(display, img.screenImages['background'])
		monocles.clear(display, img.screenImages['background'])
		player.draw(display)
		bullets.draw(display)
		monocles.draw(display)

		# detect collision
		for monocle in monocles:
			for bullet in bullets:
				if pygame.sprite.collide_mask(bullet, monocle):
					a.glass(mixer)
					bullet.kill()
					if(monocle.size > 25 + s.monocleMinSize):
						monocles.add(sprites.Monocle(monocle.size - 25, monocle.rect.center))
						monocles.add(sprites.Monocle(monocle.size - 25, monocle.rect.center))
					score += ((s.monocleMaxSize - monocle.size)%10)*100
					monocle.kill()
			if pygame.sprite.collide_mask(stache, monocle) and stache.immuneCounter <= 0:
				stache.lives -= 1;
				a.damage(mixer,stache.lives)
				stache.immuneCounter = s.fps
				
		if stache.immuneCounter > 0:
			stache.immuneCounter -= 1
		
		# advance level and add more monocles if necessary
		if(not monocles):
			level += 1
			addMoreMonocles(monocles)

		# update gui
		u.drawLevel(display, level)
		u.drawLives(display, stache.lives)
		u.drawScore(display, score)

		# determine if game is over
		if(stache.lives == 0): # win/lose condition
			gameOver = True
		
		# draw everything
		pygame.display.update()
		
		if paused:
			u.pauseGame(display)
		
		mainClock.tick(s.fps)
		  
	# stop the game and show the Game Over display
	u.drawScreen(display, 'over')
	a.playEndMusic(mixer)
	while gameOver:
		for event in pygame.event.get():
			if event.type == QUIT:
				u.terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					u.terminate()
				if event.key == K_SPACE:
					a.playGameMusic(mixer)
					gameOver = False