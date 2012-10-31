import pygame, random, math
import settingsloader as s
import bigimageloader as img

class Stache(pygame.sprite.Sprite):
	speedX = 0
	speedY = 0
	direction = 0 # in degrees
	lives = s.stacheStartingLives
	immuneCounter = 0 # determines length of temporary immunity after being hit
	firingTimer = 0 # determines if it's time to fire again

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = img.stacheImages['default']
		self.mask = pygame.mask.from_surface(self.image)

		self.rect = self.image.get_rect()
		self.rect.center = (s.windowWidth / 2, s.windowHeight / 2)

		self.direction = 90
			 
	def accelerate(self):
		self.speedX -= s.stacheMaxAcceleration * math.cos(math.radians(self.direction))
		self.speedY -= s.stacheMaxAcceleration * math.sin(math.radians(self.direction))
		if self.speedX > s.stacheMaxSpeed:
			self.speedX = s.stacheMaxSpeed
		if self.speedX < -1 * s.stacheMaxSpeed:
			self.speedX = -1 * s.stacheMaxSpeed
		if self.speedY > s.stacheMaxSpeed:
			self.speedY = s.stacheMaxSpeed
		if self.speedY < -1 * s.stacheMaxSpeed:
			self.speedY = -1 * s.stacheMaxSpeed
	  
	def decelerate(self):
		if self.speedX > 0:
			self.speedX += s.stacheDeceleration
		elif self.speedX < 0:
			self.speedX -= s.stacheDeceleration
		if self.speedY > 0:
			self.speedY += s.stacheDeceleration
		elif self.speedY < 0:
			self.speedY -= s.stacheDeceleration

		# stops when speed is really low rather than oscillating back and forth
		if math.fabs(self.speedX) <= math.fabs(s.stacheDeceleration):
			self.speedX = 0
		if math.fabs(self.speedY) <= math.fabs(s.stacheDeceleration):
			self.speedY = 0

	def fire(self):
		return Bullet(self.rect.center, self.speedX, self.speedY, self.direction)
				
	def update(self, display, thrustersOn, directionToTurn, isFiring, bullets):
		top = 0
		bottom = s.windowHeight
		left = 0
		right = s.windowWidth
		
		# if directionToTurn is -1, right. if 0, straight. if 1, left
		self.direction += s.stacheDirectionChange * directionToTurn
		
		# accelerate the stache
		if thrustersOn:
			self.accelerate()
		self.decelerate()

		# update stache image
		if thrustersOn:
			if self.immuneCounter % 15 > 7:
				baseImage = img.stacheImages['thrusterhurt']
			else:
				baseImage = img.stacheImages['thruster']
		else:
			if self.immuneCounter % 15 > 7:
				baseImage = img.stacheImages['hurt']
			else:
				baseImage = img.stacheImages['default']
		
		# rotate stache image
		center = self.rect.center
		self.image = pygame.transform.rotate(baseImage, -(self.direction - 90))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(center=center)

		# move the stache
		self.rect.x += self.speedX
		self.rect.y += self.speedY

		# move stache to opposite side if past boundary on one side
		if self.rect.center[1] >= bottom:
			self.rect.bottom = self.rect.height / 2
		elif self.rect.center[1] <= top:
			self.rect.top = bottom - self.rect.height / 2
		elif self.rect.center[0] >= right:
			self.rect.right = self.rect.width / 2
		elif self.rect.center[0] <= left:
			self.rect.left = right - self.rect.width / 2

		# mirror stache on opposite side if close to boundary on one side
		if self.rect.y > bottom-100:
			display.blit(self.image, (self.rect.x, self.rect.y - bottom), special_flags =  6)
		elif self.rect.y < top+100:
			display.blit(self.image, (self.rect.x, self.rect.y + bottom), special_flags =  6)
		elif self.rect.x > right-100:
			display.blit(self.image, (self.rect.x - right, self.rect.y), special_flags =  6)
		elif self.rect.x < left+100:
			display.blit(self.image, (self.rect.x + right, self.rect.y), special_flags =  6)
		
		display.blit(self.image, (self.rect.x + right, self.rect.y + bottom), special_flags =  6)
		
		if isFiring:
			self.firingTimer += 1
			if self.firingTimer == s.stacheFiringInterval:
				bullets.add(self.fire())
				self.firingTimer = 0
		else:
			self.firingTimer = 0
		
class Bullet(pygame.sprite.Sprite): 
	speedX = 0
	speedY = 0
	direction = 0
	lifetime = s.bulletStartingLifetime
		
	def __init__(self, initialPosition, initialSpeedX, initialSpeedY, direction):
		pygame.sprite.Sprite.__init__(self)

		self.image = img.bulletImage
		self.mask = pygame.mask.from_surface(self.image)

		self.rect = self.image.get_rect()
		self.rect.center = initialPosition
		center = self.rect.center
		self.image = pygame.transform.rotate(self.image, -(direction - 90))
		self.rect = self.image.get_rect(center=center)

		self.speedX = initialSpeedX - s.bulletLaunchSpeed * math.cos(math.radians(direction))
		self.speedY = initialSpeedY - s.bulletLaunchSpeed * math.sin(math.radians(direction))

	def update(self):
		top = 0
		bottom = s.windowHeight
		left = 0
		right = s.windowWidth

		# decrease the lifetime
		self.lifetime -= 1
		if self.lifetime < 0:
			self.kill()
			
		# move the bullet
		self.rect.x += self.speedX
		self.rect.y += self.speedY

		# rotate the bullet
		self.direction += self.speedX + self.speedY
		center = self.rect.center
		self.image = pygame.transform.rotate(img.bulletImage, self.direction)
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(center=center)

		# move bullet to opposite side if past boundary on one side
		if self.rect.center[1] >= bottom:
			self.rect.bottom = self.rect.height / 2
		elif self.rect.center[1] <= top:
			self.rect.top = bottom - self.rect.height / 2
		elif self.rect.center[0] >= right:
			self.rect.right = self.rect.width / 2
		elif self.rect.center[0] <= left:
			self.rect.left = right - self.rect.width / 2

class Monocle(pygame.sprite.Sprite):
	speedX = 0
	speedY = 0
	size = 0
	direction=0

	def __init__(self, size, initialPosition):
		pygame.sprite.Sprite.__init__(self)
		
		self.size = size
		self.direction = random.randint(0, 360)
		self.image = pygame.transform.scale(img.monocleImage, (size, size))
		self.monocleImage = self.image
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.topleft = initialPosition
		
		speed = random.randint(2, 4) * 110 / size
		self.speedX = -1 * speed * math.cos(math.radians(self.direction))
		self.speedY = -1 * speed * math.sin(math.radians(self.direction))

	def update(self):
		top = 0
		bottom = s.windowHeight
		left = 0
		right = s.windowWidth
			
		# move the monocle
		self.rect.x += self.speedX
		self.rect.y += self.speedY

		# rotate the monocle	
		baseImage = pygame.transform.scale(img.monocleImage, (self.size, self.size))
		self.direction += self.speedX + self.speedY
		center = self.rect.center
		self.image = pygame.transform.rotate(baseImage, self.direction)
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(center=center)

		# move monocle to opposite side if past boundary on one side
		if self.rect.center[1] >= bottom:
			self.rect.bottom = self.rect.height / 2
		elif self.rect.center[1] <= top:
			self.rect.top = bottom - self.rect.height / 2
		elif self.rect.center[0] >= right:
			self.rect.right = self.rect.width / 2
		elif self.rect.center[0] <= left:
			self.rect.left = right - self.rect.width / 2