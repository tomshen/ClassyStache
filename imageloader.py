# images gathered in one place, and associated rects, if appropriate

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

screenImages['background'] = pygame.image.load(os.path.join('images', 'BG.png'))
screenRects['background'] = screenImages['background'].get_rect()

screenImages['title'] = pygame.image.load(os.path.join('images', 'Title.png'))
screenRects['title'] = screenImages['title'].get_rect()

screenImages['instruct'] = pygame.image.load(os.path.join('images', 'Instruct.png'))
screenRects['instruct'] = screenImages['instruct'].get_rect()

screenImages['pause'] = pygame.image.load(os.path.join('images', 'Pause.png'))
screenRects['pause'] = screenImages['pause'].get_rect()

screenImages['over'] = pygame.image.load(os.path.join('images', 'Over.png'))
screenRects['over'] = screenImages['over'].get_rect()


# gui
digitImages = []
digitImageRects = []
for i in range(10):
	digitImages.append(pygame.image.load(os.path.join('images', str(i)+'.png')))
for i in range(10):
	digitImageRects.append(digitImages[i].get_rect())
	digitImageRects[i].top = 0
	
livesImages = []
livesImageRects = []
for i in range(s.stacheStartingLives):
	livesImages.append(pygame.image.load(os.path.join('images', str(i+1)+'Lives.png')))
for i in range(s.stacheStartingLives):
	livesImageRects.append(livesImages[i].get_rect())
	livesImageRects[i].left = 0
	livesImageRects[i].top = 0

levelImage = pygame.image.load(os.path.join('images', 'Level.png'))
levelRect = levelImage.get_rect()
	
# icon
iconImage = pygame.image.load(os.path.join('images', 'Icon.png'))