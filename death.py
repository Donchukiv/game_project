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

#parametrs
WIN_WIDTH = 500
WIN_HEIGHT = 400

#objects
pygame.init()
sc = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH), pygame.RESIZABLE)

class Death(menu):
	def __init__(self):
		super().__init__(x, y, text, h, w, click)

def main():
	while 1:
		pass