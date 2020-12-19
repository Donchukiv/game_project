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

class menu:
	def __init__(self, x, y, h=5, w=20, click = False):
		self.x = x
		self.y = y
		self.click = 


	def create_button(self, x, y, h, w,):
		pass

	def click(self, event):
		pass