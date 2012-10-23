# images gathered in one place, and associated rects, if appropriate
# for a bigger game screen (975 x 600) change import statements to use this file and change scaling in settingsloader to 1.5

import pygame, os
import settingsloader as s

# stache
stacheImages = {}
stacheImages['default'] = pygame.image.load(os.path.join('images', 'Stache.png'))
stacheImages['thruster'] = pygame.image.load(os.path.join('images', 'StacheThruster.png'))
stacheImages['hurt'] = pygame.image.load(os.path.join('images', 'StacheHurt.png'))
stacheImages['thrusterhurt'] = pygame.image.load(os.path.join('images', 'StacheThrusterHurt.png'))


# bullet
bulletImage = pygame.image.load(os.path.join('images', 'Bullet.png'))


# monocle
monocleImage = pygame.image.load(os.path.join('images', 'Mon.png'))


# screens
screenImages = {}
screenRects = {}

screenImages['background']=pygame.image.load(os.path.join('images', 'BigBG.png'))
screenRects['background']=screenImages['background'].get_rect()

screenImages['title']=pygame.image.load(os.path.join('images', 'BigTitle.png'))
screenRects['title']=screenImages['title'].get_rect()

screenImages['instruct']=pygame.image.load(os.path.join('images', 'BigInstruct.png'))
screenRects['instruct']=screenImages['instruct'].get_rect()

screenImages['pause']=pygame.image.load(os.path.join('images', 'BigPause.png'))
screenRects['pause']=screenImages['pause'].get_rect()

screenImages['over']=pygame.image.load(os.path.join('images', 'BigOver.png'))
screenRects['over']=screenImages['over'].get_rect()


# ui
scoreImages = []
scoreImageRects = []
for i in range(10):
	scoreImages.append(pygame.image.load(os.path.join('images', str(i)+'.png')))
for i in range(10):
	scoreImageRects.append(scoreImages[i].get_rect())
	scoreImageRects[i].top = 0
	
livesImages = []
livesImageRects = []
for i in range(s.stacheStartingLives):
	livesImages.append(pygame.image.load(os.path.join('images', str(i+1)+'Lives.png')))
for i in range(s.stacheStartingLives):
	livesImageRects.append(livesImages[i].get_rect())
	livesImageRects[i].left = 0
	livesImageRects[i].top = 0
	
# icon
iconImage = pygame.image.load(os.path.join('images', 'Icon.png'))