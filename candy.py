#modules
import pygame
import random
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

class candy:
	def __init__(self, cx, cy, ccolor, r = 10):
		self.x = cx
		self.y = cy
		self.r = r
		self.color = ccolor
		self.live = 1

	def appear(self, sc):
		pygame.draw.circle(sc, self.color, (self.x, self.y), self.r)
		