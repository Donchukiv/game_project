#modules
import pygame

#import death

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GREY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)

#parametrs
WIN_WIDTH = 400
WIN_HEIGHT = 500

#objects
pygame.init()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)


class bird:
	def __init__(self, x, y, r=20, color=ORANGE, vx=8, vy=0, orient = 1, shape = 1):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r = r
		self.color = color
		#self.id = pygame.draw.circle(sc, color, (x, y), r)
		self.live = 1
		self.orient = orient #orient = 1 => right, orient = -1 => left
		self.shape = shape #shape = 1 => circle, shape = 2 => square

	def appear(self):
		'''
		if self.shape == 1:
			pygame.draw.circle(sc, self.color, (self.x, self.y), self.r)
		if self.shape == 2:
			pygame.draw.rect(sc, self.color, (self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r))
			'''
		sc.blit(self.game.image, (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r))


	def move(self):
		#while self.live == 1:
		#coordinates change
			self.x = self.x + self.vx
			self.y = self.y + self.vy
			self.vy = self.vy + 0.8
			if self.x + self.r >= WIN_WIDTH or self.x - self.r <= 0:
				self.vx = (-1)*self.vx
				self.orient = (-1)*self.orient 
			
			#y velocity gets 10 up after the click
			for i in pygame.event.get():
                                if i.type == pygame.QUIT:
                                        exit()
                                elif i.type == pygame.KEYDOWN:
                                        if i.key == pygame.K_SPACE:
                                                self.vy = -10
	def death(self):
		if self.live == 0:
			pygame.time.delay(1000)
			self.yyy() 
