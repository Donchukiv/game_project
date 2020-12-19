#modules
import pygame

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)

#objects
WIN_WIDTH = 500
WIN_HEIGHT = 400
sc = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH), pygame.RESIZABLE)


pygame.init()

class bird:
	def __init__(self, x, y, r=50, color=ORANGE, vx=20, vy=0, orient = 1):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r = r
		self.color = color
		#self.id = pygame.draw.circle(sc, color, (x, y), r)
		self.live = 1
		self.orient = orient #orient = 1 => right, orient = -1 => left

	def appear(self):
		pygame.draw.circle(sc, self.color, (self.x, self.y), self.r)

	def move(self):
		#coordinates change
			self.x = self.x + self.vx
			self.y = self.y + self.vy
			self.vy = self.vy + 1
			if self.x + self.r >= WIN_WIDTH or self.x - self.r <= 0:
				self.vx = (-1)*self.vx
				self.orient = (-1) 
			#y velocity gets 10 up after the click
			'''
			for i in pygame.event.get():
				if i.type == pygame.KEYDOWN:
					if i.key == pygame.K_UP:
						self.vy = 5
'''
	def death(self):
		if hittest():
			#self.live = 0
			print('YOU DIED')
